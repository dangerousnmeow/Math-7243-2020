import dataWrangler as dw
import models as md
import pickle

import os
import argparse

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Data and model checkpoints directories					
parser.add_argument('--model_dir', type=str, default='/opt/ml/model',
                    help='directory to store checkpointed models')

# Data and model checkpoints directories					
parser.add_argument('--final_model', type=str, default='/opt/ml/model',
                    help='directory to store checkpointed models')
                    
# Data and model checkpoints directories
parser.add_argument('--data_dir', type=str, default='',
                    help='data directory containing input.txt with training examples')     
                    
args = parser.parse_args()
files = os.listdir(args.data_dir)
print(files)

##
# Need to save model weights, history to S3
##
# Save final model out to opt.
##

files = ['ID_0a336e630', 'ID_0ba79c0ef', 'ID_0bc7199c6']
#path = '../Example Bucket'


train_gen = dw.DataGenerator(folder=args.data_dir,batch_size=1, file_list=files, shuffle=False)
test_gen = dw.DataGenerator(folder=args.data_dir,batch_size=1, file_list=files, shuffle=False)

model = md.unet2D(input_size = (512,512,4))
history = md.train_model(model, train_gen, test_gen, name="model", checkpoint_dir=args.final_model, epochs=3)

print(args.final_model)

#model.save(args.final_model + '/trainedmodel.h5') # saving the model
with open(args.final_model + '/trainHistoryOld', 'wb') as handle: # saving the history of the model
    pickle.dump(history.history, handle)
