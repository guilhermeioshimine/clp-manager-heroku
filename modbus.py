from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
import time
from pyModbusTCP.client import ModbusClient
from datetime import datetime
import mysql.connector
import time
# password = Password123!
cnx = mysql.connector.connect(user='root', password='Password123!',
                              host='127.0.0.1',
                              database='demo')

SQL_ADD = 'INSERT into report (date, recipe_cod, recipe_name, solid, liquid1, liquid2, powder, blend_time) values (%s, %s, %s, %s, %s, %s, %s, %s)'

cursor = cnx.cursor()

def decimalDecoder(instance):
    if not instance.isError():
        decoder = BinaryPayloadDecoder.fromRegisters(
            instance.registers,
            byteorder=Endian.Big, wordorder=Endian.Little
        )   
        return float('{0:.2f}'.format(decoder.decode_32bit_float()))

    else:
        # Error handling.
        print("There isn't the registers, Try again.")
        return None

def stringDecoder(instance, length):
    if not instance.isError():
        decoder = BinaryPayloadDecoder.fromRegisters(
            instance.registers,
            byteorder=Endian.Big, wordorder=Endian.Little
        )   
        return decoder.decode_string(length)

    else:
        # Error handling.
        print("There isn't the registers, Try again.")
        return None
    
def stringSort(string):
    l = [x for x in string]
    it = iter(l)
    result = ''
    for x in it:
        aux = next(it)
        result += aux + x
    return result


def modbus_read():
    client = ModbusTcpClient('192.168.1.230', port=502)  # Specify the port.
    connection = client.connect()
    result = []
    if connection:
        request = client.read_holding_registers(28000, 6, unit=1)  # Specify the unit.
        codRecipe = stringDecoder(request, 6)
        codRecipe = codRecipe.decode("utf-8")
        codRecipe = stringSort(codRecipe)
        result.append(codRecipe)

        request = client.read_holding_registers(28006, 12, unit=1)  # Specify the unit.
        nameRecipe = stringDecoder(request, 12)
        nameRecipe = nameRecipe.decode("utf-8")
        nameRecipe = stringSort(nameRecipe)
        result.append(nameRecipe)

        request = client.read_holding_registers(28018, 2, unit=1)  # Specify the unit.
        solid = decimalDecoder(request)
        result.append(solid)

        request = client.read_holding_registers(28020, 2, unit=1)  # Specify the unit.
        liquid1 = decimalDecoder(request)
        result.append(liquid1)

        request = client.read_holding_registers(28022, 2, unit=1)  # Specify the unit.
        liquid2 = decimalDecoder(request)
        result.append(liquid2)

        request = client.read_holding_registers(28024, 2, unit=1)  # Specify the unit.
        powder = decimalDecoder(request)
        result.append(powder)

        request = client.read_holding_registers(28026, 1, unit=1)  # Specify the unit.
        blendTime = request.registers[0]
        result.append(blendTime)

        return result

        client.close()
    else:
        print('Connection lost, Try again')

while True:
    x = modbus_read()
    if(x):
        now = datetime.now()    
        report = (now, x[0], x[1],x[2], x[3], x[4], x[5], x[6])
        cursor.execute(SQL_ADD, report)
        cnx.commit()
        print("Salvo")
    else:
        print("Resultado Vazio")
    
        
    
    time.sleep(10)