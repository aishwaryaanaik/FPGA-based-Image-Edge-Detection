# FPGA-Based Edge Detection Using 2D Convolution  

> Real-time Sobel edge detection on **PYNQ-Z2 FPGA** using **Vitis HLS and Vivado**, achieving low-latency and efficient image processing for embedded vision applications.  

## Introduction  
This project implements **edge detection using FPGA-based 2D convolution** with the Sobel operator. By leveraging the parallel processing power of FPGAs, the design achieves **real-time image analysis** with **lower latency** and **efficient resource utilization** compared to software-only execution.  

Target applications include **Advanced Driver Assistance Systems (ADAS)**, **robotics**, and **embedded vision systems**.  

##  Features  
- Hardware-accelerated **Sobel edge detection** (3×3 kernels for Gx, Gy).  
- Implemented in **C/C++ using Vitis HLS**.  
- Integrated into **Vivado block design** with Zynq Processing System.  
- Deployment on **PYNQ-Z2 FPGA board** with Python overlay.  
- Benchmarked for **latency, LUTs, DSPs, and BRAMs**.  
# FPGA-Based Edge Detection Using 2D Convolution  

> Real-time Sobel edge detection on **PYNQ-Z2 FPGA** using **Vitis HLS and Vivado**, achieving low-latency and efficient image processing for embedded vision applications.  

## Prerequisites  

### What is Edge Detection?  
Edge detection is a fundamental step in image processing that identifies regions of rapid intensity change, which typically correspond to object boundaries or transitions in the scene.  

### Sobel Edge Detection  
The **Sobel operator** is a popular gradient-based method that uses **two 3×3 convolution kernels** (for horizontal and vertical edge detection).  

1. Convert input image → **grayscale** using:  
   \[
   Gray = 0.299R + 0.587G + 0.114B
   \]  

2. Convolve the grayscale image with **Gx** and **Gy** to compute intensity gradients:  
   \[
   Gx = I * Kx, \quad Gy = I * Ky
   \]  

3. Compute the **gradient magnitude**:  
   \[
   G = \sqrt{Gx^2 + Gy^2}
   \]  
   (In hardware, we often approximate with \(|Gx| + |Gy|\) for efficiency).  

4. Apply a **threshold** → highlight strong edges, suppress weak ones.  

The result is an image where **edges are highlighted** (white) against a dark background.
## Files required for Vitis HLS
**Xilinx Vitis HLS** (tested with version 2023.1 and above)
- **Vitis Libraries (xfopencv)**  
  - Download the Vitis Libraries from the official GitHub: [Xilinx Vitis Libraries](https://github.com/Xilinx/Vitis_Libraries)  
  - Navigate to the `vision` module (`Vitis_Libraries/vision`) which contains functions like "common/xf_common.hpp",imgproc/xf_cvt_color.hpp".  
  - Add the path of the downloaded library to your **Vitis HLS project include path**:  
    ```
    Project Settings → C/C++ Build Settings → Include Paths
    ```
    Example:  
    ```
    <path-to>/Vitis_Libraries/vision/L1/include


## Tools & Technologies  
- **Hardware:** PYNQ-Z2 FPGA  
- **Languages:** C/C++, Python  
- **Software:** Vitis HLS, Vivado, Jupyter Notebook (PYNQ)  
- **Algorithm:** Sobel Edge Detection (2D Convolution)  

## Methodology  

1. **Image Acquisition & Pre-processing**  
   - Convert RGB image → grayscale using weighted sum.  

2. **Algorithm Development in Vitis HLS**  
   - Implement Sobel edge detection in C/C++.  
   - Compute horizontal (Gx) & vertical (Gy) gradients.  
   - Apply magnitude thresholding.  

3. **IP Generation & Integration**  
   - Synthesize design in Vitis HLS.  
   - Export as IP and integrate into Vivado block design.  

4. **Bitstream Generation & Deployment**  
   - Generate `.bit` and `.hwh` files.  
   - Deploy on PYNQ-Z2 board.  

5. **Output Visualization & Benchmarking**  
   - Use Jupyter Notebook (Python) to test and visualize results.  
   - Compare FPGA vs ARM execution.  

## Results  

| Metric       | Value                  |  
|--------------|------------------------|  
| LUTs Used    | 1374                   |  
| Flip-Flops   | 580                    |  
| BRAM Blocks  | 3                      |  
| DSP Blocks   | 3                      |   

**Performance:** Outperformed ARM-only execution.  
**Efficiency:** Achieved reliable edge detection with minimal resources.  

## Applications  
- Advanced Driver Assistance Systems (ADAS)  
- Robotics & Automation  
- Smart Surveillance  
- Embedded Vision Devices  

## Future Work  
- Extend to **Canny edge detection**.  
- Implement **real-time video edge detection**.  


