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
                numeroDeSerial = usb.util.get_string(dispositivo, dispositivo.iSerialNumber)
            except usb.core.USBError:
                numeroDeSerial = "No encontrado"
            
            print(
                f"Dispositivo encontrado: VendorID={hex(dispositivo.idVendor)}, "
                f"ProductoID={hex(dispositivo.idProduct)}, Numero de Serial={numeroDeSerial}"
            )
    except usb.core.USBError as e:
        print(f"Error al acceder a dispositivos USB: {e}")

if __name__ == "__main__":
    monitoreo()

