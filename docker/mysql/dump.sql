CREATE DATABASE  IF NOT EXISTS `bookings` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bookings`;
-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: bookings
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `conference`
--

DROP TABLE IF EXISTS `conference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conference` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `floor_num` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `booked_by` varchar(1020) DEFAULT NULL,
  `booked_from` datetime DEFAULT NULL,
  `booked_to` datetime DEFAULT NULL,
  `is_santized` varchar(1020) DEFAULT NULL,
  `type` varchar(1020) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conference`
--

LOCK TABLES `conference` WRITE;
/*!40000 ALTER TABLE `conference` DISABLE KEYS */;
INSERT INTO `conference` VALUES (1,'Conference1','1',NULL,NULL,NULL,NULL,'Yes','2'),(2,'Conference2','1',NULL,NULL,NULL,NULL,'Yes','2');
/*!40000 ALTER TABLE `conference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cubicles`
--

DROP TABLE IF EXISTS `cubicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cubicles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `floor_num` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `booked_by` varchar(1020) DEFAULT NULL,
  `booked_from` datetime DEFAULT NULL,
  `booked_to` datetime DEFAULT NULL,
  `is_santized` varchar(1020) DEFAULT NULL,
  `type` varchar(1020) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cubicles`
--

LOCK TABLES `cubicles` WRITE;
/*!40000 ALTER TABLE `cubicles` DISABLE KEYS */;
INSERT INTO `cubicles` VALUES (1,'Cube1','1',NULL,NULL,NULL,NULL,'Yes','1'),(2,'Cube2','1',NULL,NULL,NULL,NULL,'Yes','1'),(3,'Cube3','1',NULL,NULL,NULL,NULL,'Yes','1'),(4,'Cube4','1',NULL,NULL,NULL,NULL,'Yes','1'),(5,'Cube1','2',NULL,NULL,NULL,NULL,'Yes','1'),(6,'Cube2','2',NULL,NULL,NULL,NULL,'Yes','1'),(7,'Cube3','2',NULL,NULL,NULL,NULL,'Yes','1'),(8,'Cube4','2',NULL,NULL,NULL,NULL,'Yes','1'),(9,'Cube1','3',NULL,NULL,NULL,NULL,'Yes','1'),(10,'Cube2','3',NULL,NULL,NULL,NULL,'Yes','1'),(11,'Cube3','3',NULL,NULL,NULL,NULL,'Yes','1'),(12,'Cube4','3',NULL,NULL,NULL,NULL,'Yes','1'),(13,'Cube4','3',NULL,NULL,NULL,NULL,'Yes','1'),(14,'Cube1','4',NULL,NULL,NULL,NULL,'No','1'),(15,'Cube2','5','Occupied','4657',NULL,NULL,'Yes','1'),(16,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(17,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(18,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(19,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(20,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(21,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(22,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(23,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(24,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1'),(25,'Cube2','6','Occupied','4657',NULL,NULL,'Yes','1');
/*!40000 ALTER TABLE `cubicles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OFFICES`
--

DROP TABLE IF EXISTS `OFFICES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OFFICES` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `floor_num` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `booked_by` varchar(1020) DEFAULT NULL,
  `is_santized` varchar(1020) DEFAULT NULL,
  `type` varchar(1020) DEFAULT NULL,
  `booked_to` datetime DEFAULT NULL,
  `booked_from` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OFFICES`
--

LOCK TABLES `OFFICES` WRITE;
/*!40000 ALTER TABLE `OFFICES` DISABLE KEYS */;
INSERT INTO `OFFICES` VALUES (1,'Alpha','1','Occupied','1260','No','4','2021-12-27 11:00:00','2021-12-27 10:25:00'),(2,'Beta','2','Occupied','1261','Yes','4','2021-12-27 11:00:00','2021-12-27 10:25:00'),(3,'Beta','1','Occupied','1261','No','4','2021-12-27 11:00:00','2021-12-27 10:25:00'),(4,'Beta','3',NULL,NULL,'No','4',NULL,NULL),(5,'Beta','4',NULL,NULL,'No','4',NULL,NULL),(6,'Beta','5',NULL,NULL,'No','4',NULL,NULL),(7,'Beta','5',NULL,NULL,'Yes','4',NULL,NULL),(8,'Alpha','3',NULL,NULL,'Yes','4',NULL,NULL),(9,'Alpha','2',NULL,NULL,'Yes','4',NULL,NULL),(10,'Alpha','4',NULL,NULL,'Yes','4',NULL,NULL),(11,'Alpha','5',NULL,NULL,'Yes','4',NULL,NULL),(12,'Gamma','1',NULL,NULL,'Yes','4',NULL,NULL),(13,'Gamma','2',NULL,NULL,'Yes','4',NULL,NULL),(14,'Gamma','3',NULL,NULL,'Yes','4',NULL,NULL),(15,'Gamma','4',NULL,NULL,'Yes','4',NULL,NULL);
/*!40000 ALTER TABLE `OFFICES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recreation`
--

DROP TABLE IF EXISTS `recreation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recreation` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `floor_num` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `booked_by` varchar(1020) DEFAULT NULL,
  `booked_from` datetime DEFAULT NULL,
  `booked_to` datetime DEFAULT NULL,
  `is_santized` varchar(1020) DEFAULT NULL,
  `type` varchar(1020) DEFAULT NULL,
  `capacity` varchar(1020) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recreation`
--

LOCK TABLES `recreation` WRITE;
/*!40000 ALTER TABLE `recreation` DISABLE KEYS */;
INSERT INTO `recreation` VALUES (1,'recreation','10',NULL,NULL,NULL,NULL,'Yes',NULL,NULL);
/*!40000 ALTER TABLE `recreation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-28 19:52:51
