drop table if exists entradas;

-- cria tabela para guardar posts do blog
create table entradas (
    id integer primary key autoincrement,
    titulo string not null,
    texto string not null
);