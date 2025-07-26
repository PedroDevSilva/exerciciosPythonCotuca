CREATE TABLE dbo.funcionario (
	id int identity not null,
	nome varchar(30) not null,
	dtaNasc smalldatetime not null,
	constraint pk_funcionario primary key (id)
);

CREATE TABLE dbo.dependente (
	id int identity not null,
	nome varchar(30) not null,
	idResponsavel int not null,
	constraint pk_dependente primary key (id),
	constraint fk_dependente_funcionario foreign key (idResponsavel) references dbo.funcionario(id)
);

--1.
SELECT * FROM dbo.funcionario;

--2.
SELECT nome FROM dbo.funcionario
	WHERE id > 10;

--3.
SELECT * FROM dbo.dependente;

--4.
SELECT * FROM dbo.dependente
	WHERE idResponsavel in (
		SELECT id FROM dbo.funcionario
		WHERE idResponsavel = id
);

--5.
SELECT nome as 'Nome do dependente de Carlos Alberto' 
	FROM dbo.dependente	
	WHERE idResponsavel in 
		(SELECT nome FROM dbo.funcionario WHERE nome ='Carlos Alberto');

--6.
SELECT d.nome as 'Nome do dependente',
	   f.nome as 'Nome do Funcionario'
	   FROM dbo.dependente d, dbo.funcionario f
	   WHERE d.idResponsavel=f.id;

--7.
SELECT d.nome as 'Nome do dependente',
	   f.nome as 'Nome do Funcionario cujo id maior que 10'
	   FROM dbo.dependente d, dbo.funcionario f
	   WHERE d.idResponsavel=f.id AND f.id > 10
;