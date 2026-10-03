# 🌐 Internet Packet Routing System

An optimized web-based network packet routing simulator built using **Python Flask** and **Tailwind CSS**, powered by **Dijkstra’s Shortest Path Algorithm** with Priority Queue optimization ($O(E \log V)$).

---

## 👥 Team Details
* **G. Rohit** (Roll No: `25MVCSDR0467`)
* **G. Ankith Yadav** (Roll No: `25MVCSDR0468`)

---

## 📌 Project Overview
In modern computer networks, routing data packets efficiently across complex topologies is vital to minimize latency and prevent network congestion. This project models communication networks as weighted directed graphs—where routers act as nodes and links act as weighted edges (latency in milliseconds)—and computes the absolute fastest transmission route in real time.

---

## ✨ Key Features
* **Optimized Algorithmic Engine:** Implements Dijkstra's Shortest Path Algorithm using Python's min-heap (`heapq`) data structure for efficient $O(E \log V)$ time performance.
* **Interactive Web Dashboard:** A responsive, modern user interface designed with Tailwind CSS allowing users to select source and destination routers effortlessly.
* **Real-Time Hop-by-Hop Routing:** Instantly outputs the complete optimal path sequence and cumulative transmission latency cost.
* **Robust Topology Modeling:** Structured adjacency list backend architecture storing multi-hop network connections and link weights.

---

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask (REST API & Server)
* **Frontend:** HTML5, Tailwind CSS (Responsive Dashboard UI)
* **Algorithm Optimization:** Python `heapq` (Min-Heap Priority Queue)
* **Development Environment:** Visual Studio Code (VS Code)
* **Version Control:** Git & GitHub (`https://github.com/gatlarohith234-dot/DAA-hackathon`)

---

## 📊 Complexity Analysis

| Complexity | Best Case | Average Case | Worst Case |
| :--- | :--- | :--- | :--- |
| **Time Complexity** | $O(1)$ / $O(\log V)$ | $O(E \log V)$ | $O((V + E) \log V)$ |
| **Space Complexity** | $O(V + E)$ | $O(V + E)$ | $O(V + E)$ |

---

## 🚀 Complete Step-by-Step Installation & Setup Guide

Follow these steps to set up, install dependencies, and run the project locally on your machine:

### Step 1: Clone the Repository
Open your terminal (or VS Code terminal) and clone the project repository:
```bash
git clone [https://github.com/gatlarohith234-dot/DAA-hackathon.git](https://github.com/gatlarohith234-dot/DAA-hackathon.git)
cd DAA-hackathon
