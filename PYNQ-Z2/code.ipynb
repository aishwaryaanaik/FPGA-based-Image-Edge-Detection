import numpy as np
from pynq import Overlay, allocate
from PIL import Image
import time
import matplotlib.pyplot as plt

def sobel_software(image):
    """Software implementation of Sobel filter using 2D convolution"""
    # Define Sobel kernels
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]], dtype=np.float32)
   
    kernel_y = np.array([[-1, -2, -1],
                         [0,  0,  0],
                         [1,  2,  1]], dtype=np.float32)
   
    # Pad the image to handle borders
    padded = np.pad(image, ((1,1), (1,1)), mode='constant')
   
    # Initialize output arrays
    grad_x = np.zeros_like(image, dtype=np.float32)
    grad_y = np.zeros_like(image, dtype=np.float32)
   
    # Perform 2D convolution
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded[i:i+3, j:j+3]
            grad_x[i,j] = np.sum(window * kernel_x)
            grad_y[i,j] = np.sum(window * kernel_y)
   
    # Calculate gradient magnitude
    gradient = np.sqrt(grad_x**2 + grad_y**2)
   
    # Normalize to 0-255 range
    gradient = np.clip(gradient, 0, 255)
    return gradient.astype(np.uint8)

def sobel_hardware(image, overlay_path="design_2.bit"):
    """Hardware implementation using PYNQ and FPGA"""
    # Load overlay
    overlay = Overlay(overlay_path)
    overlay.download()
   
    # Get reference to Sobel IP
    sobel_ip = overlay.hls_sobel_axi_stream_0
   
    # Allocate contiguous memory
    height, width = image.shape
    in_buffer = allocate(shape=(height, width), dtype=np.uint8)
    out_buffer = allocate(shape=(height, width), dtype=np.uint8)
   
    # Copy image data
    np.copyto(in_buffer, image)
    in_buffer.flush()
   
    # Configure hardware
    sobel_ip.write(0x10, in_buffer.physical_address)  # Input address
    sobel_ip.write(0x18, out_buffer.physical_address)  # Output address
    sobel_ip.write(0x20, width)  # Image width
    sobel_ip.write(0x28, height)  # Image height
    sobel_ip.write(0x00, 0x01)  # Start IP
   
    # Wait for completion
    start_time = time.time()
    while (sobel_ip.read(0x00) & 0x1):
        if time.time() - start_time > 5:
            print("Timeout waiting for IP")
            break
        time.sleep(0.01)
   
    out_buffer.invalidate()
    output = np.array(out_buffer, dtype=np.uint8)
   
    # Clean up
    in_buffer.close()
    out_buffer.close()
   
    return output

def main():
    # Load and convert image
    img_path = "test_image.jpg"
    img = Image.open(img_path).convert('L')
    img_np = np.array(img)
   
    print(f"Processing {img_path} ({img_np.shape[1]}x{img_np.shape[0]})")
   
    # Process with both methods
    print("Running software Sobel...")
    sw_start = time.time()
    sw_result = sobel_software(img_np)
    sw_time = time.time() - sw_start
   
    print("Running hardware Sobel...")
    hw_start = time.time()
    hw_result = sobel_hardware(img_np)
    hw_time = time.time() - hw_start
   
    # Display results
    plt.figure(figsize=(15, 5))
   
    plt.subplot(1, 3, 1)
    plt.imshow(img_np, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
   
    plt.subplot(1, 3, 2)
    plt.imshow(sw_result, cmap='gray')
    plt.title(f'Hardware Sobel\n({sw_time:.3f} seconds)')
    plt.axis('off')
   
    plt.subplot(1, 3, 3)
    plt.imshow(hw_result, cmap='gray')
    plt.title(f'Hardware Sobel\n({hw_time:.3f} seconds)')
    plt.axis('off')
   
    plt.tight_layout()
   
    # Save results
    Image.fromarray(sw_result).save("sobel_software.jpg")
    Image.fromarray(hw_result).save("sobel_hardware.jpg")
    print("Results saved as sobel_software.jpg and sobel_hardware.jpg")
   
    plt.show()

if __name__ == "__main__":
    main()
