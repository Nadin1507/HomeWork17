--- events
--id
--title (unique)
CREATE TABLE  IF NOT EXISTS events
(
    id    SERIAL PRIMARY KEY,
    title VARCHAR(100) UNIQUE

);


---places
--id
--address (unique)
CREATE TABLE IF NOT EXISTS places
(
    id    SERIAL PRIMARY KEY,
    addres VARCHAR(100) UNIQUE

);


---tickets
--id
--QRcode (unique)
CREATE TABLE IF NOT EXIST tickets
(
    id    SERIAL PRIMARY KEY,
    QRcode VARCHAR(100) UNIQUE

);



---events_places
--event_id --> events(id)
---place_id --> places(id)
CREATE TABLE  IF NOT EXIST events_places
(
    id    SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(id) ON DELETE CASCADE, 
    place_id INT REFERENCES places(id) ON DELETE CASCADE

);


---events_tickets
--event_id --> events(id)
--ticket_id --> tickets(id)
CREATE TABLE IF NOT EXIST events_tickets
(
    id    SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(id) ON DELETE CASCADE,
    ticket_id INT REFERENCES tickets(id)ON DELETE CASCADE

);

---many-to- many: events & places
---many-to-many: event & titckets