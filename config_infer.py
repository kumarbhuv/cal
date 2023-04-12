##################################################
# Training Config
##################################################
GPU = '0'                   # GPU
workers = 4                 # number of Dataloader workers
epochs = 150                # number of epochs
batch_size = 64            # batch size
learning_rate = 1e-3        # initial learning rate

##################################################
# Model Config
##################################################
image_size = (224, 224)     # size of training images
net = 'resnet50'  # feature extractor
num_attentions = 32         # number of attention maps
beta = 5e-2                 # param for update feature centers

visual_path = None  # './vis-cub-inception-cf/'  # None

##################################################
# Dataset/Path Config
##################################################
tag = 'aircraft'                # 'aircraft', 'bird', 'car', or 'dog'

# checkpoint model for resume training
ckpt = './FGVC/aircraft/wsdan-res50-cal/model_bestacc.pth'
