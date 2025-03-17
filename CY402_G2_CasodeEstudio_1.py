import usb.core
import usb.util

def monitoreo():
    try:
        dispositivos = list(usb.core.find(find_all=True))  
        print(f"Dispositivos USB encontrados: {len(dispositivos)}")

        if not dispositivos:
            print("No se encontraron dispositivos USB.")
            return

        for dispositivo in dispositivos:
            try:
                nombre_dispositivo = usb.util.get_string(dispositivo, dispositivo.iProduct)
            except usb.core.USBError:
                nombre_dispositivo = "No encontrado"

            try:
                numeroDeSerial = usb.util.get_string(dispositivo, dispositivo.iSerialNumber)
            except usb.core.USBError:
                numeroDeSerial = "No encontrado"

            print(
                f"Dispositivo encontrado: {nombre_dispositivo} | "
                f"VendorID={hex(dispositivo.idVendor)} | "
                f"ProductoID={hex(dispositivo.idProduct)} | "
                f"Numero de Serial={numeroDeSerial}"
            )
    except usb.core.USBError as e:
        print(f"Error al encontradar dispositivos USB: {e}")

if __name__ == "__main__":
    monitoreo()
