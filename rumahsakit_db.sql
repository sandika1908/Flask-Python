-- MariaDB dump 10.19  Distrib 10.4.19-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: rumahsakit
-- ------------------------------------------------------
-- Server version	10.4.19-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `akses`
--

DROP TABLE IF EXISTS `akses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `akses` (
  `id_akses` int(255) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id_akses`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `akses`
--

LOCK TABLES `akses` WRITE;
/*!40000 ALTER TABLE `akses` DISABLE KEYS */;
INSERT INTO `akses` VALUES (2,'Umar','asli@gmail.com','pbkdf2:sha256:260000$HeSVrQO7nlmGpRYp$f0cb00da60e3066830239e616dca43a86bb00bab375b249ae6f8ce017726d7c9'),(3,'Ujang','ujang@gmail.com','pbkdf2:sha256:260000$uE2JoJvnMUHdFivG$71a4ce67b173397a397828d9e56750c8f58e2927e0f786323087f0ca9b847b9d'),(4,'Abdul','abdul@gmail.com','pbkdf2:sha256:260000$gCt5LODMs4RULTmm$855c0c3e9ae7524b9c6a3c7b9deeace212cb1ea1a0ff5f4312ac82d91cb150c0'),(7,'Uyung','usuparta@gmail.com','pbkdf2:sha256:260000$WpI524CA7rNJxaB4$b48452eb84db7f9b49dbe51b48c3ef6f45da597b218aefb1b199e5c890f8670d'),(8,'Wanti','wanti@gmail.com','pbkdf2:sha256:260000$rpdNjXbsjtElaM0T$8fd643e68a228b93cebfcf0164e2f2ecd60cfa3fda6025bdf073862250f09730'),(9,'santi','santi@gmail.com','$2b$12$fkwPfvyT6XgcHktmwRWYyu.GErIsz38Tqdtz4mi4f14YyCIRBciyG'),(11,'dane','dane@gmail.com','$2b$12$1fPw1yC1CNGGvjoaDmJDbOyYuenspVgsn2cCObNVTroSl4/FVK/WK'),(16,'sulis','sulit@gmail.com','$2b$12$niZ6sboXc433VvuZR9bXBOadvVU8QiP3yLTgc6BT73.RTq1Eh0sP2'),(17,'joko','joko@gmail.com','$2b$12$9xVR5l7HoRXBhMMlFCzGL.wvzk/Nkt0Z9UVJX6D450qpQHOi.Qola'),(18,'samsu','samsudin@gmail.com','$2b$12$sE4OaNSNSX5gm5aAtGDMM.CEM.D9muQ.GY0nhXWDZf.VuzGEmllH6'),(19,'oji','oji@gmail.com','$2b$12$QG6CrTpyUwXcnrljuf2DHu5Qu5yC50ln0tFydl7Ee0wkE65LsT3ya'),(20,'pogba','pogba@gmail.com','$2b$12$UrLwfN7yWDOABbBzMFCtz.CWP8TC.LmvgvIHgTh0yrHcMK7Mkw7du'),(21,'catur','catur@gmail.com','$2b$12$TxQOH9oBrApJ6764aprdxuxgZBZXVwEEUATxK7qWW5tZZNmWweIg6'),(22,'tukul','tukul@gmail.com','$2b$12$veU.LmchXfodvVdmQQl5qOBiXC5IImE43YHmPkpkR9XJST7wmYubu'),(23,'popo','popo@gmail.com','$2b$12$9gBfVrTw06KglhtX080nT.vVbAvZvMHI1BsCgspkyfrc6Hl0svVFS'),(24,'dandi','dandi@gmail.com','$2b$12$p436PEPNwHGBrHim6YurWe5YyqWtQ9qiwsVlPpn.3.wK4WH/a44Qe'),(25,'bayu','bayu@gmail.com','$2b$12$u7OLoNv29bdkH19op1xhkOtS211P3a8uMqGSbye/2/H5bEijv21rC'),(26,'sandika','sandika@gmail.com','$2b$12$Rjw9GZX7AOQPKqeR/9QAPOr6GgUHa93JLjtwPzvI/7JfONg2Kq3qm'),(27,'','','$2b$12$E8q/imQllaJgU1rwW4U0luQebAhs.qTVT0t2sEIIc1zyK8FN/Aw6y'),(28,'ujo','ujo@gmail.com','$2b$12$dwlV/Nt120DivIwwwhfdZOH0TaQT5UZzO1MYFstR4PP9mlqDxbjOy');
/*!40000 ALTER TABLE `akses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dokter`
--

DROP TABLE IF EXISTS `dokter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dokter` (
  `id_dokter` int(255) NOT NULL AUTO_INCREMENT,
  `nama_dokter` varchar(255) NOT NULL,
  `id_spesialis` int(255) NOT NULL,
  `no_telp` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `pagi` enum('Pagi','Siang','Sore') NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_dokter`),
  KEY `spesialis` (`id_spesialis`),
  CONSTRAINT `dokter_ibfk_1` FOREIGN KEY (`id_spesialis`) REFERENCES `spesialis` (`id_spesialis`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dokter`
--

LOCK TABLES `dokter` WRITE;
/*!40000 ALTER TABLE `dokter` DISABLE KEYS */;
INSERT INTO `dokter` VALUES (39,'Sandika Ganteng',7,'0812913131','Jambi','Pagi','2022-11-27 15:54:38','2022-11-27 15:54:38'),(40,'Santi',9,'0812913131','Padang','Pagi','2022-11-27 15:55:24','2022-11-27 15:55:24'),(41,'Suci',7,'0812913131','Jakarta','Sore','2022-11-28 02:41:23','2022-11-28 02:41:23');
/*!40000 ALTER TABLE `dokter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kamar`
--

DROP TABLE IF EXISTS `kamar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kamar` (
  `no_kamar` int(255) NOT NULL,
  `nama_kamar` varchar(255) NOT NULL,
  `jenis_kamar` varchar(255) NOT NULL,
  `kapasitas` int(255) NOT NULL,
  `fasilitas` varchar(255) NOT NULL,
  `harga` int(255) NOT NULL,
  PRIMARY KEY (`no_kamar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kamar`
--

LOCK TABLES `kamar` WRITE;
/*!40000 ALTER TABLE `kamar` DISABLE KEYS */;
INSERT INTO `kamar` VALUES (1,'Raudah','Jenis Kamar',5,'Sofa',0),(2,'Ujang','Jenis Kamar',5,',',0),(5,'Shafa','Jenis Kamar',5,'Kulkas, Microwave',0),(7,'Marwah','Regular',3,'kulkas',0),(30,'Ujang','VIP',12,'Sofa',15000);
/*!40000 ALTER TABLE `kamar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obat`
--

DROP TABLE IF EXISTS `obat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `obat` (
  `kode_obat` int(255) NOT NULL AUTO_INCREMENT,
  `nama_obat` varchar(255) NOT NULL,
  `jenis_obat` varchar(255) NOT NULL,
  `tahun_produksi` date NOT NULL,
  `masa_berlaku` date NOT NULL,
  PRIMARY KEY (`kode_obat`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obat`
--

LOCK TABLES `obat` WRITE;
/*!40000 ALTER TABLE `obat` DISABLE KEYS */;
INSERT INTO `obat` VALUES (1,'Antimo','Jenis Obat','2022-11-17','2022-11-17'),(6,'Antasidadoen','Paten','2022-11-23','2022-11-23'),(7,'Antimo','Jenis Obat','2022-11-27','2022-11-27');
/*!40000 ALTER TABLE `obat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pasien`
--

DROP TABLE IF EXISTS `pasien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pasien` (
  `id_pasien` int(255) NOT NULL AUTO_INCREMENT,
  `nama_pasien` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  `no_telp` varchar(255) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat` varchar(255) NOT NULL,
  PRIMARY KEY (`id_pasien`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pasien`
--

LOCK TABLES `pasien` WRITE;
/*!40000 ALTER TABLE `pasien` DISABLE KEYS */;
INSERT INTO `pasien` VALUES (1,'Santi','Jenis Kelamin','085880134031','2022-11-14','lari'),(2,'Nasrul','Jenis Kelamin','123','2022-11-29','swsw'),(4,'Ade Armando','Laki-laki','303','1980-06-11','Depok'),(6,'Uyung','Jenis Kelamin','788121992121','2022-12-07','Salemba'),(7,'Joko','Laki-laki','0812913131','2022-11-14','Depok');
/*!40000 ALTER TABLE `pasien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perawat`
--

DROP TABLE IF EXISTS `perawat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perawat` (
  `id_perawat` int(255) NOT NULL AUTO_INCREMENT,
  `nama_perawat` varchar(255) NOT NULL,
  `no_telp` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(255) NOT NULL,
  PRIMARY KEY (`id_perawat`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perawat`
--

LOCK TABLES `perawat` WRITE;
/*!40000 ALTER TABLE `perawat` DISABLE KEYS */;
INSERT INTO `perawat` VALUES (1,'Joko','08121','Jenis Kelamin'),(3,'Acoy','123876','Laki-laki'),(4,'Sabrina','09812121','Perempuan');
/*!40000 ALTER TABLE `perawat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rekam_medis`
--

DROP TABLE IF EXISTS `rekam_medis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rekam_medis` (
  `id_rekam_medis` int(255) NOT NULL AUTO_INCREMENT,
  `tanggal` date NOT NULL,
  `keluhan` varchar(255) NOT NULL,
  `pemeriksaan` varchar(255) NOT NULL,
  `pengobatan` varchar(255) NOT NULL,
  PRIMARY KEY (`id_rekam_medis`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rekam_medis`
--

LOCK TABLES `rekam_medis` WRITE;
/*!40000 ALTER TABLE `rekam_medis` DISABLE KEYS */;
INSERT INTO `rekam_medis` VALUES (1,'2022-11-16','radang','dokter boyke','gausah so asik'),(2,'2022-11-10','asw','swdw','sswww'),(4,'2022-11-10','dih','swdw','sswww'),(10,'2022-11-26','asam urat','Umum','rawat inap'),(11,'2022-11-19','Diare','Umum','gausah siik');
/*!40000 ALTER TABLE `rekam_medis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spesialis`
--

DROP TABLE IF EXISTS `spesialis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spesialis` (
  `id_spesialis` int(255) NOT NULL AUTO_INCREMENT,
  `spesialis` varchar(255) NOT NULL,
  PRIMARY KEY (`id_spesialis`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spesialis`
--

LOCK TABLES `spesialis` WRITE;
/*!40000 ALTER TABLE `spesialis` DISABLE KEYS */;
INSERT INTO `spesialis` VALUES (6,'Gizi'),(7,'Fisioterapi'),(8,'Kulit'),(9,'Bedah');
/*!40000 ALTER TABLE `spesialis` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-28 13:23:20
