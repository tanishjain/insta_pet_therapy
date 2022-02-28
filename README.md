# insta_pet_therapy

Insta(nt) Pet Therapy repository for Stanford CS 236G. 
Related Instagram Page: [@logans_awesome_friends](https://www.instagram.com/logans_pawsome_friends/)

## Baseline Model (Milestone 1)

Make sure you have the relevant packages installed, including PyTorch, numpy, and matplotlib.

You must have a `dogs` directory in the project root. The directory structure should be as such:

- `dogs/`
  - `dogs/`
    - `dog.0.png`
    - `dog.1.png`
    - `...`

The baseline model was originally trained on Google Colab. Therefore, the first cell may be deleted for reproduction. Additionally, the `dataroot` in the fourth cell may be modified with the correct path to the `dogs` directory.

The dataset, Kaggle Dogs vs. Cats dataset, can be downloaded from [here](https://www.kaggle.com/c/dogs-vs-cats/data). Remember to filter out only dog images for training the model.

## BigGAN Model (Milestone 2)

The improved model implementation relies on the excellent implementation of BigGAN pretrained on ImageNet by Brock et al. \[1\] provided [here](https://github.com/ajbrock/BigGAN-PyTorch). In addition to the packages installed for the baseline model, ensure you have tqdm, scipy, and h5py installed.

Step 1. Data preprocessing. Ensure that the data is stored in the same directory structure as described earlier. Remember to run the image preprocessing step from the baseline implementation, except with the image size changed to 256.

Step 2. To improve training time, I use a pretrained model by Brock et al. \[1\] which has been pretrained on ImageNet. The model checkpoint can be found [here](https://drive.google.com/open?id=1nAle7FCVFZdix2--ks0r5JBkFnKw8ctW).

Step 3. Run the fine-tune training script (BigGAN-PyTorch/finetune.sh) to resume training the model with our dataset.

**Note:** Finetuning the model and evaluation should work as expected. However, additional functionalities from the implementation by Brock et al. \[1\] may not work as expected due to my modifications. 

### References 

\[1\] Andrew Brock, Jeff Donahue, and Karen Simonyan. “Large scale GAN training for high fidelity natural image synthesis”. In: _arXiv preprint arXiv:1809.11096_ (2018)
