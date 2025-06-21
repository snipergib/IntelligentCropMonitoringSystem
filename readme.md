# Intelligent Crop Monitoring System

An **Intelligent Crop Monitoring System** uses IoT sensor data and automated data processing to help farmers and agritech professionals continuously monitor crop conditions and make data-driven decisions. It collects environmental parameters (such as air temperature, humidity, soil moisture, light levels, etc.) and processes them in real time.  By combining Python analytics with tools like Power BI, it can **predict crop health, reduce waste, and visualize trends via dashboards**.  Such systems automate routine data tasks and improve productivity – in one study, continuous IoT-based monitoring was shown to yield **“improved crop yield and productivity” with negligible human intervention**.  This project is aimed at farmers, agronomists, or researchers who need a smart, automated solution for tracking crop and environmental data over time.

## Key Features

* **Environmental Sensing:** Collects real-time data from field/greenhouse sensors (temperature, humidity, soil moisture, CO₂, light, etc.).  This enables continuous monitoring of key crop-environment variables without manual measurement.
* **Automated Data Pipeline:** Orchestrates a full ETL (Extract-Transform-Load) workflow. A *sensor simulator* or actual hardware supplies raw data, which is then cleaned (`data_cleaning.py`), aggregated (e.g. daily averages), and loaded into a database (`csv_loader.py`/`database.py`).  All steps can be triggered together via `pipeline_runner.py`.
* **Data Cleaning & Transformation:** Raw sensor and external data are preprocessed to remove noise and fill missing values. The pipeline produces files like `cleaned_sensor_data.csv`, `daily_avg_sensor_data.csv`, and a final `transformed_crop_data.csv` containing merged sensor and crop datasets.
* **External Data Integration:** Includes a `web_scraper.py` module to fetch relevant crop or weather data from online sources.  Combined with sensor readings, this enriches the dataset for analysis or decision support.
* **Data Analytics & Visualization:** Uses Python (with libraries like pandas) and Power BI for analysis. It can **“predict crop health, reduce waste, and visualize trends via dashboards”**.  For example, the processed data can be loaded into a BI tool to generate charts or alerts for growers.
* **Sensor Simulation (Test Mode):** Offers a simulation mode (`sensor_simulator.py`) to generate fake sensor readings.  This allows testing the pipeline on a regular computer without needing physical hardware.
* **Database Storage:** Persistently stores all readings in a database (e.g. SQLite or MySQL) via `database.py`. This makes querying historical data or integrating with other systems easy.

## Technologies Used

* **Programming:** Python 3 (primary language for scripts).
* **Libraries:** Common data libraries (e.g., `pandas`, `numpy` for data handling), `requests`/`BeautifulSoup` for web scraping, and a DB-API library (like `sqlite3` or `mysql-connector`) for database access.
* **Hardware (Optional):** IoT devices such as Arduino or Raspberry Pi can host the system. For example, a Raspberry Pi running Linux can collect sensor data and execute the Python scripts.  Typical sensors might include DHT11/DHT22 (temp/humidity), soil moisture probes, light sensors, etc.
* **Database:** A relational database (SQLite or MySQL) to store time-series sensor data.
* **Cloud/IoT Platform:** The system could be extended to use an IoT cloud platform (e.g. ThingSpeak, AWS IoT) for data collection and alerts, though the current code uses local storage.
* **Data Visualization:** Power BI or similar tools to build dashboards and reports from the processed data.
* **Operating System:** Any OS that supports Python (Linux, Windows, or macOS). For embedded deployment, Raspberry Pi OS or Arduino-like environments are suitable.

## Installation & Setup Instructions

1. **Clone the repository.**

   ```bash
   git clone https://github.com/snipergib/IntelligentCropMonitoringSystem.git
   cd IntelligentCropMonitoringSystem
   ```
2. **Set up Python environment.** (Recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: .\venv\Scripts\activate
   ```
3. **Install dependencies.**

   ```bash
   pip install -r requirements.txt
   ```

   *(The `requirements.txt` should list needed libraries like pandas, requests, BeautifulSoup, etc.)*
4. **Configure database (if needed).** By default, the code may use SQLite. If you prefer MySQL or PostgreSQL, update `database.py` accordingly and install the appropriate DB connector. Ensure the database is created and accessible.
5. **(Optional) Connect hardware sensors.** If running on a microcontroller or SBC, wire your sensors (temperature, humidity, soil moisture, etc.) to the device’s GPIO pins. Modify the sensor input code if using real hardware. Otherwise, use the simulator.
6. **Run the pipeline.** Use the provided scripts to start collecting/processing data:

   ```bash
   # (Optional) Simulate sensor data without real hardware
   python sensor_simulator.py
   # Run the full data pipeline (cleaning, scraping, loading, etc.)
   python pipeline_runner.py
   ```

   The pipeline will generate cleaned CSV files and update the database.

## Usage Guide

* **Processing Data:** After setup, execute `pipeline_runner.py` (as above) to run the entire workflow. This will read raw data (or simulated data), clean and aggregate it, fetch any external crop data, and save the results.
* **Viewing Results:** Check the output CSV files (e.g. `daily_avg_sensor_data.csv`, `transformed_crop_data.csv`) or query the database to analyze the data. You can load these into Excel, a BI tool, or any data analysis environment.
* **Real-Time Monitoring:** To continuously monitor data, you might set up a scheduler (cron job or task scheduler) that runs `pipeline_runner.py` at regular intervals.
* **Dashboard & Alerts:** With the data stored and cleaned, you can build Power BI or other dashboards to visualize trends. You could also extend the system to send email/text alerts based on thresholds (e.g. low soil moisture).
* **Example:**

  ```bash
  # Run data pipeline
  python pipeline_runner.py
  # Open the final dataset in a viewer or analysis tool
  cat transformed_crop_data.csv
  ```
* **Extensibility:** You can customize the `web_scraper.py` to gather specific crop information or use APIs (e.g. weather services). The modular scripts make it easy to add new sensors or processing steps.

## Folder Structure

* `sensor_simulator.py` – Generates fake sensor readings (timestamped) and writes to CSV for testing.
* `web_scraper.py` – Fetches external crop/environment data (e.g. from websites or APIs) and saves it.
* `data_cleaning.py` – Reads raw sensor and crop data, performs cleaning (e.g. handling missing values) and preprocessing.
* `csv_loader.py` – Loads prepared CSV data into the database (creating tables or inserting records).
* `database.py` – Defines the database connection and schema; contains functions to insert or query data.
* `pipeline_runner.py` – Main orchestrator script. It calls the simulator (or real data input), cleaning, scraping, and loading scripts in sequence.
* `*.csv` files – Example datasets and outputs used/produced by the pipeline. For instance:

  * `crop_data.csv`: Example input data about crop conditions.
  * `cleaned_sensor_data.csv`: Sensor readings after cleaning.
  * `daily_avg_sensor_data.csv`: Aggregated daily averages of sensors.
  * `transformed_crop_data.csv`: Final merged dataset (sensor + crop data).
* `requirements.txt` – Lists Python dependencies (e.g., pandas, requests, BeautifulSoup).
* `readme.md` – (This file) Project documentation.

## License

This project currently has **no license file**. 

## Contributing

Contributions are welcome! If you find bugs or have ideas for improvements, please open an issue or pull request on the GitHub repository. You can contribute by:

* Forking the repo and submitting a pull request with your changes.
* Reporting issues or feature requests via the GitHub **Issues** page.
* Suggesting enhancements (e.g., new sensor types, data sources, or analysis routines).

Please make sure your code follows the existing style and includes documentation for any new features.

## Contact / Author

This project was created by **Earnest S** (GitHub username: *snipergib*). For questions or collaboration, you can open an issue on GitHub or reach out via my GitHub profile. Additional information about my work is available on my [portfolio](http://earni.onrender.com).
