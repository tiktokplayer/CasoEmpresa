
CREATE TABLE `asignacion` (
  `ID_ASIGNACION` int(11) NOT NULL,
  `ID_DEPARTAMENTO` int(11) NOT NULL,
  `ID_EMPLEADO` int(11) NOT NULL



CREATE TABLE `departamento` (
  `ID_DEPARTAMENTO` int(11) NOT NULL,
  `NOM_DEPARTAMENTO` varchar(20) NOT NULL,
  `ID_EMPLEADO` int(11) NOT NULL



CREATE TABLE `empleado` (
  `ID_EMPLEADO` int(11) NOT NULL,
  `NOM_EMPLEADO` varchar(100) NOT NULL,
  `CORREO` varchar(50) NOT NULL,
  `TELEFONO` int(11) NOT NULL,
  `DIRECCION` varchar(100) NOT NULL,
  `RUT` int(11) NOT NULL,
  `FECHA_NACIMIENTO` varchar(12) NOT NULL,
  `FECHA_CONTRATO` varchar(12) NOT NULL,
  `SALARIO` int(11) NOT NULL,
  `ID_TIPO_EMPLEADO` int(11) NOT NULL,
  `ID_ROLES` int(11) NOT NULL,
  `PASSWORD_EMP` varchar(20) NOT NULL



CREATE TABLE `informe` (
  `ID_INFORME` int(11) NOT NULL,
  `ID_EMPLEADO` int(11) NOT NULL,
  `FECHA_HORA` varchar(25) NOT NULL,
  `REPORTE` varchar(800) NOT NULL



CREATE TABLE `modulos` (
  `ID_MODULOS` int(11) NOT NULL,
  `NOM_MODULOS` varchar(30) NOT NULL



CREATE TABLE `proyecto` (
  `ID_PROYECTO` int(11) NOT NULL,
  `NOM_PROYECTO` varchar(50) NOT NULL,
  `DES_PROYECTO` varchar(100) NOT NULL,
  `FECHA_INICIO` varchar(12) NOT NULL,
  `FECHA_FIN` varchar(12) NOT NULL



CREATE TABLE `proyecto_empleado` (
  `ID_PRO_EMPLEADO` int(11) NOT NULL,
  `ID_EMPLEADO` int(11) NOT NULL,
  `ID_PROYECTO` int(11) NOT NULL



CREATE TABLE `registro_tiempo` (
  `ID_REGISTRO` int(11) NOT NULL,
  `ID_PRO_EMPLEADO` int(11) NOT NULL,
  `FECHA` varchar(12) NOT NULL,
  `CANTIDAD_HORAS` int(11) NOT NULL,
  `DES_REG_TIEMPO` varchar(200) NOT NULL,
  `HORAS_EXTRAS` tinyint(1) NOT NULL,
  `OBSERVACION` varchar(500) NOT NULL



CREATE TABLE `roles` (
  `ID_ROLES` int(11) NOT NULL,
  `ROL` varchar(30) NOT NULL,
  `PERMS_TXT` varchar(200) NOT NULL



CREATE TABLE `tipo_empleado` (
  `ID_TIPO_EMPLEADO` int(11) NOT NULL,
  `IDENTIFICACION` int(11) NOT NULL





ALTER TABLE `asignacion`
  ADD PRIMARY KEY (`ID_ASIGNACION`),
  ADD KEY `ID_DEPARTAMENTO` (`ID_DEPARTAMENTO`,`ID_EMPLEADO`);


ALTER TABLE `departamento`
  ADD PRIMARY KEY (`ID_DEPARTAMENTO`),
  ADD KEY `ID_EMPLEADO` (`ID_EMPLEADO`);


ALTER TABLE `empleado`
  ADD PRIMARY KEY (`ID_EMPLEADO`),
  ADD KEY `ID_TIPO_EMPLEADO` (`ID_TIPO_EMPLEADO`,`ID_ROLES`),
  ADD KEY `ID_ROLES` (`ID_ROLES`);


ALTER TABLE `informe`
  ADD PRIMARY KEY (`ID_INFORME`),
  ADD KEY `ID_EMPLEADO` (`ID_EMPLEADO`);


ALTER TABLE `modulos`
  ADD PRIMARY KEY (`ID_MODULOS`);


ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`ID_PROYECTO`);


ALTER TABLE `proyecto_empleado`
  ADD PRIMARY KEY (`ID_PRO_EMPLEADO`),
  ADD KEY `ID_EMPLEADO` (`ID_EMPLEADO`,`ID_PROYECTO`);


ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`ID_REGISTRO`),
  ADD KEY `ID_PRO_EMPLEADO` (`ID_PRO_EMPLEADO`);


ALTER TABLE `roles`
  ADD PRIMARY KEY (`ID_ROLES`);


ALTER TABLE `tipo_empleado`
  ADD PRIMARY KEY (`ID_TIPO_EMPLEADO`);
