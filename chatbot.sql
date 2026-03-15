-- database/chatbot.sql

CREATE DATABASE IF NOT EXISTS college_chatbot;
USE college_chatbot;

CREATE TABLE IF NOT EXISTS faqs ( 
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat_history (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_message TEXT,
  bot_reply TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/* Sample FAQs for RIMT */
INSERT INTO faqs (question, answer) VALUES
('admission dates', 'Admission dates are usually from July to September. Check the admission office for exact dates.'),
('courses offered', 'RIMT offers B.Tech (CSE, ECE, ME, CE), MBA, MCA, BBA, BCA, and Diploma courses.'),
('library timing', 'Library is open from 9 AM to 8 PM Monday to Saturday.'),
('contact', 'RIMT Bareilly, Pilibhit Road. Phone: +91-XXXXXXXXXX. Visit www.rimt.ac.in for more details.');
