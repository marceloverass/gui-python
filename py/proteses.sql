-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 07-Abr-2023 às 16:37
-- Versão do servidor: 10.4.22-MariaDB
-- versão do PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `proteses`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `proteses`
--

CREATE TABLE `proteses` (
  `id` int(11) NOT NULL,
  `numeroid` int(15) NOT NULL,
  `supinf` varchar(1) NOT NULL,
  `cliente` varchar(50) NOT NULL,
  `dataentrega` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `proteses`
--

INSERT INTO `proteses` (`id`, `numeroid`, `supinf`, `cliente`, `dataentrega`) VALUES
(35, 5555, 'S', 'Dr Paulo', '29/05/2001');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `proteses`
--
ALTER TABLE `proteses`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `proteses`
--
ALTER TABLE `proteses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
