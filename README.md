Ditto Ryanda
JCDSVL 07

This project is a Python-based Command Line Interface (CLI) application developed by Ditto Ryanda as part of Capstone Project 1 (Purwadhika, JCDSVL07). It enables users to manage warehouse inventory using basic CRUD (Create, Read, Update, Delete) operations. Users can view all available products or search for a specific item using its code, add new items with input validation, update specific fields (name, quantity, cost price, or selling price), and delete items from the inventory with confirmation prompts to avoid accidental deletion. The system is fully interactive through a numbered menu and is designed for ease of use during manual warehouse stock management. While the current version uses a list of dictionaries for in-memory storage, potential improvements include implementing persistent storage (e.g., saving to JSON or CSV), adding a login system, generating inventory reports, or building a simple GUI or web-based interface.

Product format example : 
{
  'kode': 'KD1',
  'nama': 'buku',
  'jumlah': 60,
  'modal': 50000,
  'harga': 75000
}
