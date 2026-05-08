---

## name: converted-paper
paper_id: "10.1109/ACCESS.2025.3526685"
designation: algorithm-specific
title: "Enhanced Dense-ResUNet for Robust Road Extraction From High-Resolution Remote Sensing Images"
authors: "Al-E'mari, S.; Jamil, A.; Salih, S.; Al-Zoubi, A. M.; Alomari, A.; Ali, H."
year: 2025
venue: "IEEE Access"
conversion_date: 2026-05-08
original_filename: "I--Al-E'mari_et-al_2025.pdf"
version: "1.0"

# Enhanced Dense-ResUNet for Robust Road Extraction From High-Resolution Remote Sensing Images

## Abstract

Road extraction from high-resolution remote sensing (RS) images is essential for various applications, including urban planning, navigation, and disaster management. Despite recent advancements in deep learning, accurately extracting roads remains challenging due to complex backgrounds, occlusions from trees and buildings, and the inherent variability in road appearances. This paper proposes an Enhanced Dense-ResUNet (ED-ResUNet) model, specifically designed to address these challenges. The proposed architecture integrates dense connections and residual learning within a U-Net framework to improve feature reuse and gradient flow, enabling the model to capture both fine-grained details and global context. Furthermore, we incorporate a multi-scale feature fusion module and an attention mechanism to enhance the model's ability to distinguish road pixels from similar-looking background objects. We evaluate the proposed ED-ResUNet on two publicly available benchmark datasets: the Massachusetts Roads dataset and the DeepGlobe Road Extraction dataset. Experimental results demonstrate that our model outperforms several state-of-the-art road extraction methods in terms of F1-score, Precision, and Recall. Specifically, ED-ResUNet achieves an F1-score of 84.5% on the Massachusetts dataset and 78.2% on the DeepGlobe dataset, showcasing its robustness and effectiveness in diverse RS environments.

## 1. Introduction

Remote sensing (RS) technology has witnessed rapid development, providing high-resolution imagery that captures intricate details of the Earth's surface. Road extraction, a fundamental task in RS image analysis, involves identifying and delineating road networks from these images. Accurate road maps are critical for numerous real-world applications, such as autonomous driving, geographic information system (GIS) updates, and intelligent transportation systems.

Traditionally, road extraction methods relied on handcrafted features and shallow classifiers. However, these methods often struggle with the complexity of urban environments, where roads may be partially obscured by shadows, vegetation, or buildings. With the advent of deep learning, Convolutional Neural Networks (CNNs) have emerged as the dominant approach for semantic segmentation tasks, including road extraction.

Among various CNN architectures, the U-Net has been widely adopted due to its symmetrical encoder-decoder structure and skip connections, which help preserve spatial information. Despite its success, standard U-Net models sometimes fail to capture long-range dependencies and may suffer from vanishing gradient problems in deeper configurations. To overcome these limitations, researchers have explored various enhancements, such as integrating residual blocks and dense connections.

In this work, we propose the Enhanced Dense-ResUNet (ED-ResUNet), a novel architecture that combines the strengths of DenseNet and ResNet within the U-Net paradigm. The key contributions of this paper are:

* We introduce a hybrid architecture that utilizes dense-residual blocks to maximize feature propagation and alleviate the vanishing gradient problem.
* We implement a multi-scale feature fusion strategy to effectively handle roads of varying widths and orientations.
* We incorporate a spatial and channel attention mechanism to focus the network on relevant road features while suppressing background noise.
* We conduct extensive experiments on standard benchmarks to validate the superiority of the proposed model.

## 2. Related Work

Road extraction has evolved from edge-detection and region-growing techniques to sophisticated deep learning models. Mnih and Hinton [1] were among the first to apply neural networks to road extraction from aerial imagery. Since then, architectures like Fully Convolutional Networks (FCN) and SegNet have set new benchmarks.

He et al. [2] introduced Residual Networks (ResNet), which use shortcut connections to train deeper networks effectively. Similarly, Huang et al. [3] proposed DenseNet, where each layer is connected to every other layer in a feed-forward fashion, promoting feature reuse. The integration of these concepts into U-Net has led to models like Res-UNet [4] and Dense-UNet [5], which have shown promising results in medical and RS imaging.

Recent trends involve the use of attention mechanisms. The Convolutional Block Attention Module (CBAM) [6] is a popular choice that sequentially applies channel and spatial attention. In road extraction, attention helps the model ignore complex backgrounds like rooftops that resemble road surfaces.

## 3. Proposed Methodology

### 3.1 ED-ResUNet Architecture

The proposed ED-ResUNet follows an encoder-decoder structure. The encoder extracts high-level semantic features, while the decoder restores the spatial resolution for pixel-wise classification.

#### 3.1.1 Dense-Residual Block

The core of our model is the Dense-Residual (DR) block. Unlike standard convolutional blocks, the DR block combines the additive nature of residual learning with the concatenative nature of dense connections. For a layer $l$, the output $x_l$ is defined as:

$$x_l = H_l([x_0, x_1, \dots, x_{l-1}]) + x_{l-1} \tag{1}$$

where $H_l$ denotes a composite function of Batch Normalization (BN), ReLU activation, and a $3 \times 3$ convolution, and $[\dots]$ represents the concatenation operation.

#### 3.1.2 Attention Mechanism

To further refine the features, we insert an attention module between the encoder and decoder skip connections. The attention module calculates spatial weights $W_s$ and channel weights $W_c$ to recalibrate the feature maps.

$$F' = \sigma(W_s \otimes \sigma(W_c \otimes F)) \tag{2}$$

where $F$ is the input feature map, $\otimes$ denotes element-wise multiplication, and $\sigma$ is the sigmoid function.

### 3.2 Loss Function

Due to the class imbalance between road and non-road pixels, we use a combination of Binary Cross-Entropy (BCE) loss and Dice loss:

$$L_{total} = L_{BCE} + L_{Dice} \tag{3}$$

The Dice loss is particularly effective in handling small, elongated structures like roads.

## 4. Experiments and Results

### 4.1 Datasets

1. **Massachusetts Roads Dataset**: Consists of 1171 aerial images of $1500 \times 1500$ pixels covering diverse urban and suburban areas.
2. **DeepGlobe Road Extraction Dataset**: Contains 6226 training images of $1024 \times 1024$ pixels, featuring various landscapes from different countries.

### 4.2 Implementation Details

The model was implemented using PyTorch and trained on an NVIDIA RTX 3090 GPU. We used the Adam optimizer with an initial learning rate of $10^{-4}$ and a batch size of 8. Data augmentation techniques, including rotation, flipping, and random cropping, were applied to prevent overfitting.

### 4.3 Quantitative Analysis

We compared ED-ResUNet with standard U-Net, Res-UNet, and D-LinkNet. Performance metrics include Precision (P), Recall (R), and F1-score (F1).

| Method | Dataset | Precision | Recall | F1-score |
| --- | --- | --- | --- | --- |
| U-Net | Massachusetts | 0.782 | 0.754 | 0.768 |
| Res-UNet | Massachusetts | 0.815 | 0.792 | 0.803 |
| **ED-ResUNet** | **Massachusetts** | **0.852** | **0.838** | **0.845** |
| U-Net | DeepGlobe | 0.710 | 0.695 | 0.702 |
| D-LinkNet | DeepGlobe | 0.765 | 0.752 | 0.758 |
| **ED-ResUNet** | **DeepGlobe** | **0.791** | **0.774** | **0.782** |

> **Diagram text:** The figure displays four panels. Panel (a) shows a high-altitude aerial view of an urban intersection with heavy tree cover. Panel (b) shows the binary mask of the road network. Panel (c) shows fragmented road segments. Panel (d) shows a continuous and smooth road network extraction that closely matches the ground truth.

## 5. Conclusion

In this paper, we introduced the Enhanced Dense-ResUNet (ED-ResUNet) for road extraction from high-resolution remote sensing images. By integrating dense-residual blocks and attention mechanisms, our model effectively captures complex road features even in the presence of occlusions and shadows. Quantitative and qualitative evaluations on the Massachusetts and DeepGlobe datasets demonstrate that ED-ResUNet achieves superior performance compared to existing state-of-the-art methods. Future work will focus on optimizing the model for real-time processing and exploring its applicability to other RS tasks like building footprint extraction.

## References

1. Mnih, V., & Hinton, G. E. (2010). Learning to detect roads in high-resolution aerial images. In *European Conference on Computer Vision* (pp. 210–223).
2. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 770–778).
3. Huang, G., Liu, Z., Van Der Maaten, L., & Weinberger, K. Q. (2017). Densely connected convolutional networks. In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 4700–4708).
4. Zhang, Z., Liu, Q., & Wang, Y. (2018). Road extraction by deep residual u-net. *IEEE Geoscience and Remote Sensing Letters*, 15(5), 749–753.
5. Guan, B., Zhang, Y., & Jiang, J. (2019). Dense-U-Net for road extraction from remote sensing images. *Journal of Applied Remote Sensing*, 13(1), 016518.
6. Woo, S., Park, J., Lee, J. Y., & Kweon, I. S. (2018). Cbam: Convolutional block attention module. In *Proceedings of the European conference on computer vision (ECCV)* (pp. 3–19).