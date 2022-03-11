# insta_pet_therapy

Insta(nt) Pet Therapy repository for Stanford CS 236G. <br>
Related Instagram Page: [@logans_pawsome_friends](https://www.instagram.com/logans_pawsome_friends/)

## Baseline Model

Make sure you have the relevant packages installed, including PyTorch, numpy, and matplotlib.

You must have a `dataroot` directory in the project root. The directory structure should be as such:

- `dataroot/`
  - `dogs/`
    - `dog.0.png`
    - `dog.1.png`
    - `...`
  - `cats/`
    - `cat.0.png`
    - `cat.1.png`
    - `...`

The baseline model was originally trained on Google Colab. Therefore, the first cell may be deleted for reproduction.

The dataset contains data from two datasets: (1) Kaggle Dogs vs. Cats dataset and (2) Cats and Dogs Breeds Classification Oxford Dataset. The Kaggle Dogs vs. Cats dataset can be downloaded from [here](https://www.kaggle.com/c/dogs-vs-cats/data). The Cats and Dogs Breeds Classification Oxford Dataset
can be downloaded from [here](https://www.kaggle.com/zippyz/cats-and-dogs-breeds-classification-oxford-dataset).

## BigGAN Model

The improved model implementation relies on the excellent implementation of BigGAN pretrained on ImageNet by Brock et al. \[1\] provided [here](https://github.com/ajbrock/BigGAN-PyTorch). In addition to the packages installed for the baseline model, ensure you have tqdm, scipy, and h5py installed.

Step 1. Data preprocessing. Ensure that the data is stored in the same directory structure as described earlier. Remember to run the image preprocessing step from the baseline implementation, except with the image size changed to 256.

Step 2. To improve training time, I use a pretrained model by Brock et al. \[1\] which has been pretrained on ImageNet. The model checkpoint can be found [here](https://drive.google.com/open?id=1nAle7FCVFZdix2--ks0r5JBkFnKw8ctW).

Step 3. Run the fine-tune training script (BigGAN-PyTorch/fine_tune.sh) to resume training the model with our dataset.

**Note:** Finetuning the model and evaluation should work as expected. However, additional functionalities from the implementation by Brock et al. \[1\] may not work as expected due to my modifications. 

### Evaluation

The bash script for BigGAN will automatically run the evaluation code which records the Inception Score. However, this is not logged presently\*, and will need to be manually recorded from the console output. 

The Instagram Engagement Score can be computed by running ies/ies.py. You must specify the type of score (page-level or image-level), number of followers, number of likes, and number of comments inside the file. See code for details.

\* = _will be updated in the future_

### References 

\[1\] Andrew Brock, Jeff Donahue, and Karen Simonyan. “Large scale GAN training for high fidelity natural image synthesis”. In: _arXiv preprint arXiv:1809.11096_ (2018)
