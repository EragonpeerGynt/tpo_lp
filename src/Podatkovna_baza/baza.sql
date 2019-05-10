-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tpolp
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `tpolp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tpolp` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `tpolp`;

--
-- Table structure for table `Uporabnik`
--

DROP TABLE IF EXISTS `Uporabnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Uporabnik` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `mail` varchar(30) NOT NULL,
  `geslo` varchar(30) NOT NULL,
  `status` int(1) NOT NULL,
  `potrjen` int(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Uporabnik`
--

LOCK TABLES `Uporabnik` WRITE;
/*!40000 ALTER TABLE `Uporabnik` DISABLE KEYS */;
INSERT INTO `Uporabnik` VALUES (0,'andreja@gmail.com','MojeGeslo',0,0),(1,'blaz@gmail.com','NjegovoGeslo',1,1),(2,'katja@gmail.com','NjenoGeslo',2,1),(3,'regina@gmail.com','NjenoGeslo2',0,1);
/*!40000 ALTER TABLE `Uporabnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vnosKoledar`
--

DROP TABLE IF EXISTS `vnosKoledar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vnosKoledar` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(16) NOT NULL,
  `opis` text NOT NULL,
  `trajanje` int(2) NOT NULL,
  `zacetek` datetime NOT NULL,
  `idU` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`idU`) REFERENCES `Uporabnik`(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vnosKoledar`
--

LOCK TABLES `vnosKoledar` WRITE;
/*!40000 ALTER TABLE `vnosKoledar` DISABLE KEYS */;
INSERT INTO `vnosKoledar` VALUES (1,'Kolokvij PUI','Kolokvij iz predmeta PUI',1,'2019-06-09 14:00:00',3),(2,'PZ TPO','Preverjanje znanja iz TPO',1,'2019-05-23 09:00:00',3);
/*!40000 ALTER TABLE `vnosKoledar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vnosUrnik`
--

DROP TABLE IF EXISTS `vnosUrnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vnosUrnik` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(16) NOT NULL,
  `barva` int(1) NOT NULL,
  `trajanje` int(2) NOT NULL,
  `zacetek` time NOT NULL,
  `dan` varchar(3) NOT NULL,
  `idU` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`idU`) REFERENCES `Uporabnik`(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vnosUrnik`
--

LOCK TABLES `vnosUrnik` WRITE;
/*!40000 ALTER TABLE `vnosUrnik` DISABLE KEYS */;
INSERT INTO `vnosUrnik` VALUES (1,'PUI',2,3,'12:00:00','CET',3),(2,'TPO',3,3,'09:00:00','CET',3),(3,'BMO',7,3,'11:00:00','PON',3);
/*!40000 ALTER TABLE `vnosUrnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vnosTODO`
--

DROP TABLE IF EXISTS `vnosTODO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vnosTODO` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `vsebina` text NOT NULL,
  PRIMARY KEY (`id`),
  `idU` int(10) NOT NULL,
  FOREIGN KEY (`idU`) REFERENCES `Uporabnik`(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vnosTODO`
--

LOCK TABLES `vnosTODO` WRITE;
/*!40000 ALTER TABLE `vnosTODO` DISABLE KEYS */;
INSERT INTO `vnosTODO` VALUES (1,'To bojo sedaj moji zapiski.',3), (2,'V četrtek ne smem pozabiti narediti domače naloge za v petek.',3), (3,'Ta link mi pomaga pri dn za MAT: www.nekajnekaj.si',3);
/*!40000 ALTER TABLE `vnosTODO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dogodek`
--

DROP TABLE IF EXISTS `dogodek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dogodek` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ime` varchar(30) NOT NULL,
  `datum` date NOT NULL,
  `organizator` varchar(20) NOT NULL,
  `opis` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dogodek`
--

LOCK TABLES `dogodek` WRITE;
/*!40000 ALTER TABLE `dogodek` DISABLE KEYS */;
INSERT INTO `dogodek` VALUES (1,'Škisova', '2019-05-09','Škis','Škisova tržnica na temni strani Ljubljane');
/*!40000 ALTER TABLE `dogodek` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-01 15:05:05
