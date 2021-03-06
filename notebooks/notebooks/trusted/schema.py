# -*- coding: utf-8 -*-
"""Schema.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYoKC4uNlVFy2WXO4AVAIvlAWY2BG1yQ
"""

create table usageData(
	landCode char(15) not null,
	zoneCode bigint,
	locationCode integer,
	mainUSage char(50),
	totalArea numeric(2),
	builtArea numeric (2),
	price bigint,
	primary key (landCode)
)

create table stratification(
	landCode char(15) not null,
	areaCode bigint,
	stratumCode integer,
	primary key (landCode),
	foreign key (landCode) references usageData(landCode)
)