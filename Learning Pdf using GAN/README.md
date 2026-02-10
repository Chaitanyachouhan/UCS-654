# Learning Probability Density Functions using Data Only

**Course:** UCS-654 Assignment - Advance Mathematics  
**Student Roll Number:** 102316106  

---

## 1. Objective
To learn an unknown probability density function (PDF) of a transformed random variable $z$ implicitly using a Generative Adversarial Network (GAN), without assuming any parametric form (like Gaussian or Exponential). This assignment demonstrates the capability of GANs to approximate complex, non-standard distributions derived from real-world data.

---

## 2. Dataset
- **Feature Used:** NO₂ concentration ($x$) from air quality data.
- **Source:** [India Air Quality Data on Kaggle](https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data)
- **Preprocessing:** Cleaning missing values and extracting the `no2` feature column.

---

## 3. Methodology

### Step 1: Data Transformation
The input feature $x$ is transformed into a new variable $z$ using a deterministic non-linear function derived specifically from the University Roll Number.

**Transformation Function:**
$$ z = T(x) = x + a_r \cdot \sin(b_r \cdot x) $$

**Parameter Derivation for Roll No: 102316106**
The parameters $a_r$ and $b_r$ are calculated as:
- $r = 102316106$
- $a_r = 0.5 + (r \pmod 7) = 0.5 + 4 = 2.0$
- $b_r = 0.3 \cdot ((r \pmod 5) + 1) = 0.3 \cdot (1 + 1) = 0.6$

**Final Transformation Applied:**
$$ z = x + 2.0 \cdot \sin(0.6 \cdot x) $$

### Step 2: GAN Architecture
A standard GAN architecture was implemented to model the distribution of $z$.

**Generator (G):**
- **Input:** Noise vector ($z_{noise}$) of dimension 1 sampled from a standard normal distribution $N(0, 1)$.
- **Architecture:** 
  - Linear Layer (1 $\to$ 16) $\to$ ReLU
  - Linear Layer (16 $\to$ 16) $\to$ ReLU
  - Output Layer (16 $\to$ 1)
- **Role:** Maps random noise to the data space of $z$.

**Discriminator (D):**
- **Input:** Sample value (real $z$ or fake $z_f$).
- **Architecture:** 
  - Linear Layer (1 $\to$ 16) $\to$ ReLU
  - Linear Layer (16 $\to$ 16) $\to$ ReLU
  - Output Layer (16 $\to$ 1) $\to$ Sigmoid Activation
- **Role:** Distinguishes between real samples from the dataset and fake samples from the Generator.

### Step 3: Training Configuration
- **Loss Function:** Binary Cross Entropy (BCELoss).
- **Optimizer:** Adam (Learning Rate = 0.001, betas default).
- **Epochs:** 20,000.
- **Batch Size:** 128.
- **Device:** CPU/GPU (implementation uses PyTorch).

---

## 4. Results and Visualization

The training process involved optimizing the min-max objective function. The Generator successfully learned to map the Gaussian noise to the target distribution of $z$.

### Key Observations:
1.  **Mode Coverage:** The GAN captured the multi-modal nature of the transformed distribution effectively.
2.  **Training Stability:** The training showed stable convergence, with the Discriminator and Generator reaching an equilibrium state (Discriminator loss $\approx 1.38$, Generator loss $\approx 0.69$).
3.  **PDF Approximation:** The Kernel Density Estimation (KDE) of the generated samples closely approximates the density of the real transformed data $z$.

### Final Visualization
The image below summarizes the entire process:
1.  Original Distribution of $x$.
2.  Transformed Distribution of $z$.
3.  The non-linear mapping $x \to z$.
4.  Comparison of Real vs. Generated Histograms.
5.  Learned Probability Density Function (PDF).

![Final GAN Results](image/final_gan_results.png)

---

## 5. Submission Details
- **Transformation Parameters:** $a_r = 2.0$, $b_r = 0.6$
- **Code:** Implemented in `PDF_102316106 (1).ipynb` using PyTorch.
- **Result:** The GAN samples match the statistical properties of the transformed dataset.
