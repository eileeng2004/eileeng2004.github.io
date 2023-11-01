class Persona:
    contador_personas =0

    def __init__(self, nombre:str, apellido:str, cedula:str, correo:str) :
        self._nombre=nombre
        self._apellido=apellido
        self._cedula=cedula
        self._correo=correo

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido

    @property
    def cedula (self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula=cedula

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

if __name__ == '__main__':
    objPersona1 = Persona (nombre= 'Eileen', apellido='Gonzalez', cedula='0943308221', correo='geileen@mail.com')
    print(objPersona1.__str__())


class Empleado (Persona):
    contador_empleados=0

    def __init__(self, id_empleado, sueldo, nombre, apellido, cedula):
        self._id_empleado=id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado {self.__dict__.__str__()}'

if __name__== '__main__':
    e1 = Empleado(nombre='Eileen', apellido='Gonzalez', sueldo='1500', cedula='595577584', id_empleado=1)
    print(e1)


class Cliente:
    contador_cliente = 0

    def __init__(self, nombre, apellido, fecha_registro, vip):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def __str__(self):
        return f'Cliente: {self.__dict__.__str__()}'


if __name__ == '__main__':
    cli1 = Cliente(nombre='Eileen', apellido='Gonzalez', fecha_registro='13-10-2023', vip=True)
    print(cli1)
    cli2 = Cliente(nombre='Javier', apellido='Torres', fecha_registro='29-10-2023', vip=False)
    print(cli2)