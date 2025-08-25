## PYNQ-Z2 Board  

The **PYNQ-Z2** is an FPGA development board based on the **Xilinx Zynq-7000 SoC**.  
It combines a **dual-core ARM Cortex-A9 processor** with programmable logic (FPGA), making it suitable for both **embedded software** and **hardware acceleration**.  

### Key Features  
- **Processor**: Dual-core ARM Cortex-A9 (650 MHz).  
- **FPGA Fabric**: Xilinx Zynq XC7Z020-1CLG400C.  
- **Memory**: 512 MB DDR3 RAM.  
- **Storage**: MicroSD card slot.  
- **Connectivity**:  
  - HDMI In/Out  
  - Ethernet (10/100/1000 Mbps)  
  - USB OTG and UART  
  - Audio In/Out  
- **GPIO**: 2 × Pmod connectors, Arduino shield connector, LEDs, buttons, and switches.  

###  Why We Use It  
- Allows deployment of **FPGA-accelerated algorithms** (e.g., convolution, signal processing, ML inference).  
- Python productivity with PYNQ framework for easy development.  
- Suitable for **real-time applications** like oversteering detection and ADAS projects.  

###  Resources  
- [PYNQ-Z2 Official Page](http://www.tul.com.tw/ProductsPYNQ-Z2.html)  
- [PYNQ Documentation](https://pynq.io/)  


## Using PYNQ-Z2 Board with Direct Ethernet Connection

### 1. Connect PYNQ-Z2 to Laptop via Ethernet
- Plug an Ethernet cable between your laptop and the PYNQ-Z2 board.
- Power on the board using a 5V/2.5A adapter.
- Configure your laptop’s Ethernet adapter with a static IP on the same subnet as the board, for example:
  - Laptop IP: `192.168.2.1`
  - Subnet mask: `255.255.255.0`
- The board usually has a default IP: `192.168.2.99`.

### 2. Test Connection
- Open a terminal/command prompt on your laptop:
ping 192.168.2.99.

### 3. Access Jupyter Notebook

- Open a web browser and go to:

http://192.168.2.99:9090


- You should see the PYNQ Jupyter dashboard.

- From here, you can upload your Vivado files (.bit, .hwh, .xsa) and notebooks.

### 4. Load Vivado Overlay

In a new notebook, run:

```python
from pynq import Overlay

# Load your bitstream
overlay = Overlay("/home/xilinx/vivado_files/my_design.bit")
overlay.download()
