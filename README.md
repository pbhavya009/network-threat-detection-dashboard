🛡️ Network Threat Detection Dashboard

A SOC-style dashboard built using the **Elastic Stack (Elasticsearch + Kibana)** to monitor and visualize network threats, suspicious ports, and anomalies in real-time.

🚀 Features
- Real-time log visualization from network or simulated data  
- Detection of top source and destination IPs  
- Identification of frequently blocked or suspicious ports  
- Protocol-based traffic insights  
- Exportable Kibana dashboard (`export.ndjson`)

  # Step 1: Run Elasticsearch & Kibana
sudo service elasticsearch start
sudo service kibana start

# Step 2: Run the Python script to send data
python3 log_sender.py

# Step 3: Import dashboard in Kibana
Management → Saved Objects → Import → upload export.ndjson

# Step 4: Open the dashboard and watch live data!


🧩 Tech Stack
-Elasticsearch — Data indexing and search  
-Kibana — Visualization and dashboard creation  
-Elastic Agent — Data collection and forwarding  

🧠 How to Import Dashboard
1. Download the file `export.ndjson` from this repository.  
2. In **Kibana**, navigate to:Stack Management → Saved Objects → Import
3. Upload the `export.ndjson` file.  
4. Your dashboard will appear under **Analytics → Dashboard**.

## 📸 Screenshots
See the screenshots included in this repo to preview the dashboard layout.

"Author"
Bhavya Puri
Cybersecurity Intern | SOC Analyst Trainee  
[LinkedIn](https://www.linkedin.com/in/bhavya-puri-31227027a/)  
[GitHub](https://github.com/pbhavya009)


