import sqlite3
from constants import DB_NAME


pregunta_1 = """
select 
    j.jurisdiction_name,
    dc.cause_name, 
    SUM(total) as total_deseases 
        from jurisdictiondeathcause s_jdc 

    left join jurisdiction j  on j.jurisdiction_id=s_jdc.jurisdiction_id 
    left join  deathcause dc on dc.deathcause_id=s_jdc.deathcause_id 

    where j.jurisdiction_name = "United States"
    /* si  no se  quieren ignorar los grupos de causas comentar  la siguiente linea*/ 
    and dc.cause_name not in ("All Cause","Natural Cause") 
    
    group by  s_jdc.jurisdiction_id,s_jdc.deathcause_id
    order by s_jdc.total desc
    limit 10
"""
pregunta_2 = """
select 
    year,
    dc.cause_name,
    SUM(total)  
        from jurisdictiondeathcause jdc 

    left join  deathcause dc on dc.deathcause_id=jdc.deathcause_id 

    where jdc.year=2017 
    /* si  no se  quieren ignorar los grupos de causas comentar  la siguiente linea*/ 
    and dc.cause_name not in ("All Cause","Natural Cause") 
    group by  jdc.jurisdiction_id,jdc.deathcause_id
    order by SUM(total) desc
    limit 1

"""
pregunta_3 = """
select
    year,
    sum(total) as total
        from jurisdictiondeathcause s_jdc 

    left join  deathcause dc on dc.deathcause_id=s_jdc.deathcause_id
    where cause_name ='All Cause'
    group by year,cause_name

"""

pregunta_4 = """
select
f.year, 
cast (sum(drug_overdose) as REAL )/cast (sum(all_cause) as REAL)*100  as pct 
from
    (select 
        year,
        case when dc.cause_name = 'All Cause' then sum(total) end as 'all_cause' ,
        case when dc.cause_name = 'Drug Overdose' then sum(total) end as 'drug_overdose' 
            from jurisdictiondeathcause s_jdc 
        left join  deathcause dc on dc.deathcause_id=s_jdc.deathcause_id
        where cause_name in ('All Cause', 'Drug Overdose')
        group by year,cause_name) f

        group by f.year
    

"""
pregunta_5 = """

select  year ,sum(Jan) ,sum(Dec)  from 
    (select 
        year,
        case when month = 1 then total end as Jan,
        case when month = 12 then total end as Dec
        from jurisdictiondeathcause s_jdc 
        left join  deathcause dc on dc.deathcause_id=s_jdc.deathcause_id
        where cause_name ='All Cause' and month in (1,12)
        group by year,month,cause_name
    ) f

    group by f.year
    having  sum(Jan) < sum(Dec) ;

"""

def execute_and_print(conn,query):
    results = conn.execute(query)
    for k in results:
        print(k)
conn = sqlite3.connect(DB_NAME)
preguntas = [pregunta_1,pregunta_2,pregunta_3,pregunta_4,pregunta_5]
for index,pregunta in enumerate(preguntas):
    print(f'Pregunta : {index +1 }')
    execute_and_print(conn,pregunta)

