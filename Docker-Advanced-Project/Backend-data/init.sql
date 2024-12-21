-- Create a table named 'items'
CREATE TABLE items (
    id SERIAL PRIMARY KEY,       -- Auto-incrementing ID
    name TEXT NOT NULL           -- Name of the item
);

-- Insert sample data into the 'items' table
INSERT INTO items (name) VALUES 
('Sample Item 1'),
('Sample Item 2'),
('Sample Item 3');
