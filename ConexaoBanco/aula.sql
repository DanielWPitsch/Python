create database aula;
use aula;

CREATE TABLE `tb_cliente` (
  `id` smallint(6) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `nome_rua` varchar(60) DEFAULT NULL,
  `bairoo` varchar(40) DEFAULT NULL,
  `cep` int(11) NOT NULL,
  `cpf` varchar(15) DEFAULT NULL,
  `uf` enum('ac','al','ap','am','ba','ce','df','es','go','ma','mt','ms','mg','pa','pb','pr','pe','pi','rj','rn','rs','ro','rr','sc','sp','se','to') DEFAULT NULL,
  `telefone` int(11) NOT NULL,
  `desconto` decimal(3,1) DEFAULT NULL,
  `sexo` enum('m','f') DEFAULT NULL
) ;

--
-- Despejando dados para a tabela `tb_cliente`
--

INSERT INTO `tb_cliente` (`id`, `nome`, `nome_rua`, `bairoo`, `cep`, `cpf`, `uf`, `telefone`, `desconto`, `sexo`) VALUES
(1, 'José', 'Das flores', 'Centro', 454, '111', 'rn', 987118, NULL, 'm'),
(2, 'Pires da Silva', 'Do rio', 'Grotão', 565, '222', 'pb', 123478, NULL, 'm'),
(3, 'Mariana', 'Do horizonte', 'Derba', 573, '333', 'ba', 765432, 5.0, 'f'),
(4, 'Yasmin Moneta', 'Do litoral', 'Ondina', 762, '444', 'ba', 223444, NULL, 'f'),
(5, 'Igor Ralf', 'Do interior', 'Marés', 656, '555', 'rj', 556677, 3.0, 'm'),
(6, 'Pedro', 'Conselheiro da silva', 'Amaralina', 656, '666', 'ba', 654333, NULL, 'm'),
(7, 'Mariana Dantas', 'Das flores', 'Cristo', 456, '777', 'pb', 222111, NULL, 'f'),
(8, 'Isabelle Silva', 'Caimbinhas', 'Manaira', 456, '888', 'pb', 112277, NULL, 'f'),
(9, 'Wilson Souza', 'Ilariê', 'Bessa', 322, '999', 'pb', 987889, 10.0, 'm'),
(10, 'Everton Alves', 'Derba', 'Bessa', 134, '007', 'pb', 767676, 8.0, 'm'),
(11, 'Pedro Lima', 'Titanic afundou', 'Manaira', 567, '998', 'pb', 568009, NULL, 'm'),
(12, 'Antonio Jose', 'Segundo turno', 'Centro', 453, '765', 'sp', 900087, 2.0, 'm'),
(13, 'Pierre Matias', 'Do rio', 'Centro', 222, '443', 'sp', 808070, NULL, 'm'),
(14, 'Elder de Oliveira', 'Luiza Dantas', 'Zé Americo', 58071000, '055', 'pb', 88888888, 99.9, 'm'),
(15, 'Moneta Alves', 'Das flores', 'Marés', 356, '134', 'rj', 260921, 11.0, 'f');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_fabricante`
--

CREATE TABLE `tb_fabricante` (
  `codigo` smallint(6) NOT NULL,
  `nome` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_fabricante`
--

INSERT INTO `tb_fabricante` (`codigo`, `nome`) VALUES
(100, 'Hp'),
(101, 'Dell'),
(102, 'Apple'),
(103, 'Itautec'),
(104, 'Xerox'),
(105, 'Samsung'),
(106, 'Sony');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_item_pedido`
--

CREATE TABLE `tb_item_pedido` (
  `codigoproduto` smallint(6) NOT NULL,
  `idpedido` smallint(6) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_item_pedido`
--

INSERT INTO `tb_item_pedido` (`codigoproduto`, `idpedido`, `quantidade`) VALUES
(3, 1, 5),
(4, 2, 12),
(5, 4, 10),
(10, 2, 22),
(12, 5, 4),
(14, 8, 5);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_pedido`
--

CREATE TABLE `tb_pedido` (
  `id` smallint(6) NOT NULL,
  `tipopagamento` varchar(100) NOT NULL,
  `idcliente` smallint(6) DEFAULT NULL,
  `dataentrada` date NOT NULL,
  `dataembarque` date NOT NULL,
  `desconto` int(11) DEFAULT NULL,
  `valortotal` decimal(8,2) NOT NULL,
  `telefone` int(11) NOT NULL,
  `formapagamento` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_pedido`
--

INSERT INTO `tb_pedido` (`id`, `tipopagamento`, `idcliente`, `dataentrada`, `dataembarque`, `desconto`, `valortotal`, `telefone`, `formapagamento`) VALUES
(1, 'À vista', 8, '2017-05-12', '2018-06-12', 5, 3346.00, 11, 'Cash'),
(2, 'Cartão', 5, '2015-01-02', '2016-03-12', NULL, 987.00, 22, 'Dividido'),
(3, 'Boleto', 12, '2012-03-24', '2013-04-02', 3, 8765.00, 33, 'Total'),
(4, 'Boleto', 3, '2018-05-13', '2018-07-12', 3, 5436.00, 44, 'Total'),
(5, 'Cartão', 5, '2016-06-11', '2017-08-21', NULL, 5414.00, 55, 'Dividido'),
(6, 'Cartão', 3, '2018-09-16', '2018-10-24', NULL, 8761.00, 66, 'Vencimento'),
(7, 'Cartão', 6, '2015-04-29', '2016-05-02', NULL, 651.00, 77, 'Vencimento'),
(8, 'À Vista', 3, '2018-10-21', '2018-10-28', 5, 6700.00, 88, 'Cash'),
(9, 'Cartão', 4, '2014-11-21', '2015-12-23', NULL, 6529.00, 99, 'dividido');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_produto`
--

CREATE TABLE `tb_produto` (
  `codigo` smallint(6) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `preco` decimal(8,2) DEFAULT NULL,
  `fabricante` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_produto`
--

INSERT INTO `tb_produto` (`codigo`, `nome`, `preco`, `fabricante`) VALUES
(1, 'Iphone x', 6856.00, 102),
(2, 'Laptop', 10234.00, 103),
(3, 'Monitor', 846.00, 101),
(4, 'Impressora', 765.00, 100),
(5, 'Impressora', 987.00, 104),
(6, 'Mouse', 79.00, 105),
(7, 'Teclado', 87.00, 103),
(8, 'Tv 20”', 1987.00, 106),
(9, 'Tv 59”', 4987.00, 105),
(10, 'Monitor led', 960.00, 100),
(11, 'Monitor ', 787.00, 102),
(12, 'impressora', 867.00, 104),
(13, 'Projetor multimídia', 1087.00, 106),
(14, 'Iphone 7', 4987.00, 102),
(15, 'Macbook ', 14987.00, 102);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_vendedor`
--

CREATE TABLE `tb_vendedor` (
  `codigo` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `salario` decimal(8,2) NOT NULL,
  `telefone` int(11) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL
) ;

--
-- Despejando dados para a tabela `tb_vendedor`
--

INSERT INTO `tb_vendedor` (`codigo`, `nome`, `salario`, `telefone`, `sexo`) VALUES
(1, 'Radagondes Oliveira', 856.00, 98771234, 'm'),
(2, 'Esmeraldina Silva', 1234.00, 89870909, 'f'),
(3, 'Antonieta Silvestre', 2146.00, 98716542, 'f'),
(4, 'Joselino Pedro Cabral', 1765.00, 99985454, 'm'),
(5, 'Fulustreco de Amaral', 987.00, 90877667, 'm'),
(6, 'Zefilina Xavier', 1000.00, 98984252, 'f'),
(7, 'Dom Manuel ', 1987.00, 98790182, 'm');

select * from tb_cliente;
select nome, salario from tb_vendedor;
select nome, preco, codigo from tb_produto;
select nome, preco, codigo from tb_produto where preco > 1000;

select nome as Produto, preco as Preço, codigo as Código
from tb_produto where preco > 1000;

select nome as 'Produto Disponivel', preco as 'Preço do Produto', codigo as 'Código do Produto'
from tb_produto where preco > 1000;

select nome, telefone, 'Aviso previo' as Condição
from tb_vendedor where salario >= 2000;

select nome as Colaborador, salario as 'Salário Atual',
salario*1.3 as 'Salário com Aumento' from tb_vendedor;

select max(salario) from tb_vendedor;
select avg(salario) from tb_vendedor;

select * from tb_pedido;
select tipopagamento, telefone from tb_pedido
where valortotal > 5000 and valortotal < 8000;

select tipopagamento, telefone from tb_pedido
where valortotal between 5436 and 6700.87;

select * from tb_produto;
select preco, fabricante from tb_produto
where nome='Monitor' or nome='Laptop' or nome='Iphone X';

select preco, fabricante from tb_produto
where nome IN ('monitor', 'laptop', 'iphone x');

select * from tb_pedido;
select tipopagamento, valortotal, formapagamento
from tb_pedido
where dataentrada between '2018-01-01' and '2018-12-31';

select tipopagamento, valortotal, formapagamento
from tb_pedido order by tipopagamento asc;
#default é asc

select bairoo,uf,nome from tb_cliente
where nome like 'm%';

select bairoo,uf,nome from tb_cliente
where nome like '%a';

select count(*) quantidade, uf from tb_cliente group by uf;