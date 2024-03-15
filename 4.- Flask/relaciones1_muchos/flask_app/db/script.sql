-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_salones
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_salones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_salones` DEFAULT CHARACTER SET utf8 ;
USE `esquema_salones` ;

-- -----------------------------------------------------
-- Table `esquema_salones`.`salones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_salones`.`salones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_salon` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_salones`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_salones`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_completo` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `salon_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_usuarios_salones_idx` (`salon_id` ASC),
  CONSTRAINT `fk_usuarios_salones`
    FOREIGN KEY (`salon_id`)
    REFERENCES `esquema_salones`.`salones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
