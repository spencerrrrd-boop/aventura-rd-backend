-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: aventura-rd-db-spencerrrrd-b42a.b.aivencloud.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.4.8

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'dd3a43d8-5a36-11f1-9060-0ea6d28b3e5f:1-39';

--
-- Table structure for table `administradores`
--

DROP TABLE IF EXISTS `administradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administradores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_administradores_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administradores`
--

LOCK TABLES `administradores` WRITE;
/*!40000 ALTER TABLE `administradores` DISABLE KEYS */;
INSERT INTO `administradores` VALUES (1,'Administrador AventuraRD','admin@aventurard.com','$2b$12$D/r7/3T2X9DDlQNqpIiA7O/CzruMXV0dHnKFaxlbllMydFBWGPAD.',1,'2026-05-28 02:06:58');
/*!40000 ALTER TABLE `administradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `ix_categorias_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Senderismo','Rutas y trekking por la naturaleza dominicana','2026-05-28 02:06:57'),(2,'Rafting','Descenso de ríos y rápidos emocionantes','2026-05-28 02:06:57'),(3,'Zipline','Canopy y tirolesas sobre el bosque','2026-05-28 02:06:57'),(4,'Escalada','Escalada en roca y montaña','2026-05-28 02:06:57'),(5,'Camping','Noches bajo las estrellas en la naturaleza','2026-05-28 02:06:57'),(6,'Ciclismo','Mountain bike por senderos y montañas','2026-05-28 02:06:57');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ofertas`
--

DROP TABLE IF EXISTS `ofertas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ofertas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `descripcion` text NOT NULL,
  `imagen_url` varchar(500) DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `duracion_dias` int NOT NULL,
  `destino` varchar(200) NOT NULL,
  `itinerario` text,
  `cupos_disponibles` int NOT NULL,
  `activa` tinyint(1) DEFAULT NULL,
  `categoria_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categoria_id` (`categoria_id`),
  KEY `ix_ofertas_id` (`id`),
  CONSTRAINT `ofertas_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ofertas`
--

LOCK TABLES `ofertas` WRITE;
/*!40000 ALTER TABLE `ofertas` DISABLE KEYS */;
INSERT INTO `ofertas` VALUES (1,'Trekking Pico Duarte','La aventura más desafiante de República Dominicana. Sube al pico más alto del Caribe a través de senderos únicos rodeados de pinos y naturaleza virgen.','https://images.unsplash.com/photo-1551632811-561732d1e306?w=800',4500.00,3,'La Ciénaga, La Vega','Día 1: Llegada y campamento base. Día 2: Ascenso al pico (3,098 msnm). Día 3: Descenso y regreso.',12,1,1,'2026-05-28 02:06:57','2026-05-28 02:06:57'),(2,'Rafting Río Yaque del Norte','Adrenalina pura en el río más largo del Caribe. Navega rápidos emocionantes rodeado de la exuberante naturaleza de Jarabacoa.','https://images.unsplash.com/photo-1530866495561-507c9faab2ed?w=800',2800.00,1,'Jarabacoa, La Vega','08:00 Llegada. 09:00 Briefing de seguridad. 10:00 Descenso del río (3 horas). 13:00 Almuerzo incluido. 15:00 Regreso.',15,1,2,'2026-05-28 02:06:58','2026-05-28 02:06:58'),(3,'Zipline Jarabacoa','Vuela sobre el bosque tropical dominicano a más de 80 km/h. Una experiencia de tirolesa incomparable con vistas espectaculares al valle de Jarabacoa.','https://images.unsplash.com/photo-1521673461164-de300ebcfb17?w=800',1500.00,1,'Jarabacoa, La Vega','09:00 Llegada. 09:30 Equipo y seguridad. 10:00 Circuito de 8 cables (2 horas). 12:00 Fin de la actividad.',20,1,3,'2026-05-28 02:06:58','2026-05-28 02:06:58'),(4,'Escalada Salto de Jimenoa','Combina escalada en roca con una de las cascadas más bellas de República Dominicana. Perfecto para aventureros con experiencia básica.','https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800',3200.00,2,'Jarabacoa, La Vega','Día 1: Llegada, escalada en roca y campamento. Día 2: Visita al Salto de Jimenoa y regreso.',8,1,4,'2026-05-28 02:06:58','2026-05-28 02:06:58'),(5,'Camping Valle Nuevo','Duerme bajo un cielo lleno de estrellas en el Parque Nacional Valle Nuevo a 2,200 metros de altura. Una experiencia única de desconexión total.','https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800',2000.00,2,'Constanza, La Vega','Día 1: Llegada, senderismo y fogata. Día 2: Amanecer en el valle, desayuno y regreso.',10,1,5,'2026-05-28 02:06:58','2026-05-28 02:06:58'),(6,'MTB Constanza','Recorre los senderos de montaña de Constanza en bicicleta todo terreno. Paisajes únicos de pinos, fresas y vegetación de altura que no encontrarás en otro lugar del Caribe.','https://images.unsplash.com/photo-1544191696-102dbdaeeaa0?w=800',1800.00,1,'Constanza, La Vega','08:00 Llegada. 08:30 Selección de bicicleta y ruta. 09:00 Recorrido de 25km (4 horas). 13:00 Almuerzo y regreso.',12,1,6,'2026-05-28 02:06:58','2026-05-28 02:06:58');
/*!40000 ALTER TABLE `ofertas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_cliente` varchar(100) NOT NULL,
  `apellido_cliente` varchar(100) NOT NULL,
  `email` varchar(200) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `oferta_id` int NOT NULL,
  `fecha_reserva` date NOT NULL,
  `num_personas` int NOT NULL,
  `total_pago` decimal(10,2) NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `estado` enum('pendiente','confirmada','cancelada','completada') DEFAULT NULL,
  `notas` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oferta_id` (`oferta_id`),
  KEY `ix_reservas_id` (`id`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`oferta_id`) REFERENCES `ofertas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-28 19:43:41
