-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `Member` varchar(40) NOT NULL,
  `PRN_NO` varchar(45) NOT NULL,
  `ID` varchar(45) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Address1` varchar(45) DEFAULT NULL,
  `Address2` varchar(45) DEFAULT NULL,
  `PostId` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `BookId` varchar(45) DEFAULT NULL,
  `BookTitle` varchar(45) DEFAULT NULL,
  `Auther` varchar(45) DEFAULT NULL,
  `DateBorrowed` varchar(45) DEFAULT NULL,
  `DateDue` varchar(45) DEFAULT NULL,
  `DaysOnBook` varchar(45) DEFAULT NULL,
  `LateReturnFine` varchar(45) DEFAULT NULL,
  `DateOverDue` varchar(45) DEFAULT NULL,
  `FinalPrice` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PRN_NO`,`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('Lecturer','123','23','sdfg','asdfg','delhi','hjbbh','755','hjbj','GDGD','Advance','Het','2023-09-18 15:51:52.075880','2023-10-03 15:51:52.075880','15','Rs.50','NO','Rs.159'),('Lecturer','146','66496','fdfe','ssd','OK','sdsds6522','254155','12365698','BKID54','Introduction to Python','j.k shah','2023-09-18 10:24:46.345283','2023-09-28 10:24:46.345283','15','Rs.50','NO','Rs.75'),('Lecturer','146GCGGGHVJ','66496','fdfe','ssd','DK','sdsds6522','OK','12365698','ABS5454','Jungle','Elite','2023-09-18 15:46:49.122529','2023-10-03 15:46:49.122529','15','Rs.50','NO','Rs.250'),('Lecturer','21661531','351564','5','566','5tky','gfmjf','564','645','ABC','Joss Guru','Guru','2023-09-15 14:02:57.577766','2023-09-30 14:02:57.577766','15','Rs.50','NO','Rs.150'),('Admin Staff','684','849','xfgxh','xfdhx','568','8654573456','zesx','rzytr','BKID5454','Python Manual','Paul Berry','2023-09-18 12:26:51.224487','2023-10-03 12:26:51.224487','15','Rs.50','NO','Rs.788'),('Admin Staff','8779','54','456','46','318','1549646531','46','13','BKID5454','Python Manual','Paul Berry','2023-09-18 14:31:00.773327','2023-10-03 14:31:00.773327','15','Rs.50','NO','Rs.788');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-18 16:00:57
