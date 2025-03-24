import psycopg2


DB_Config = {
      "dbname": "Servis_reserv_tickets_db",
      "user": "postgres",
      "password": "password",
      "host": "localhost",
      "port": "5432"
}

def connect_db():
    return  psycopg2.connect(**DB_Config)

def init_db():

 def get_all_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM event")

        events = cur.fetchall()
        print(events)
        print(type(events)
            CREATE TABLE events
            (
               id    SERIAL PRIMARY KEY,
               title VARCHAR(100) UNIQUE
            );
        """)

        cur.execute("""
             CREATE TABLE places
            (
               id    SERIAL PRIMARY KEY,
               addres VARCHAR(100) UNIQUE
        )
        );
            """)
        cur.execute("""
              CREATE TABLE tickets
             (
                 id    SERIAL PRIMARY KEY,
                 QRcode VARCHAR(100) UNIQUE

              );

             """)

        cur.execute("""
                CREATE TABLE events_places
                (
                    id    SERIAL PRIMARY KEY,
                    event_id INT REFERENCES events(id) ON DELETE CASCADE,
                    place_id INT REFERENCES places(id) ON DELETE CASCADE

                );

            """)

        cur.execute("""
              CREATE TABLE events_tickets
              (
                     id    SERIAL PRIMARY KEY,
                     event_id INT REFERENCES events(id) ON DELETE CASCADE,
                     ticket_id INT REFERENCES tickets(id)ON DELETE CASCADE

              );

            """)