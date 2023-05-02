import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1234",
    database="postgres"
)
cur = conn.cursor()

Q1 = """
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern text)
    RETURNS SETOF Phonebook AS $$
    DECLARE
        result_row Phonebook%ROWTYPE;
    BEGIN
        FOR result_row IN SELECT * FROM Phonebook WHERE name ILIKE '%' || pattern || '%' OR CAST(number AS TEXT) LIKE '%' || pattern || '%' LOOP
            RETURN NEXT result_row;
        END LOOP;
        RETURN;
    END;
    $$ LANGUAGE plpgsql
    
"""
#cur.execute("SELECT * FROM search_by_pattern('1')")
