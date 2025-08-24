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
