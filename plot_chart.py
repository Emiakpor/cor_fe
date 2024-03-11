import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot(loss_history, val_loss_history, accuracy_history, val_accuracys_history,
               x_test_prop_class_count, pred_digits_prop_class_count_pre_label, y_test_prop_class_count_actual_label,
                 x_test_mis_class_count, pred_digits_mis_class_count_pre_label, y_test_mis_class_count_actual_label,
            labels, _confusion_matrix):

    plt.figure(figsize=(12, 12))
    plt.style.use('ggplot')
    # plt.subplot(2,2,1)
    plt.plot(loss_history)
    plt.plot(val_loss_history)
    plt.title('Loss of the Model')
    plt.ylabel('Loss', fontsize=12)
    plt.xlabel('Epoch', fontsize=12)
    plt.legend(['train loss', 'validation loss'], loc='best', prop={'size': 12})

    plt.figure(figsize=(12, 12))
    plt.style.use('ggplot')
    # plt.subplot(2,2,2)
    plt.plot(accuracy_history)
    plt.plot(val_accuracys_history)
    plt.title('Accuracy of the Model')
    plt.ylabel('Accuracy', fontsize=12)
    plt.xlabel('Epoch', fontsize=12)
    plt.legend(['train accuracy', 'validation accuracy'], loc='lower right', prop={'size': 12})

    prop_class_len = len(x_test_prop_class_count)

    count=0
    fig,ax=plt.subplots(4,2)
    fig.set_size_inches(15,15)
    if x_test_prop_class_count :
        for i in range (4):
            for j in range (2):
                if count < prop_class_len :
                    ax[i,j].imshow(x_test_prop_class_count[count])
                    ax[i,j].set_title(str(pred_digits_prop_class_count_pre_label[count])
                                    +"\n"+ str(y_test_prop_class_count_actual_label[count]))
                    
                    plt.tight_layout()

                count+=1


    mis_class_len = len(x_test_mis_class_count)
    count=0
    fig,ax=plt.subplots(4,2)
    fig.set_size_inches(15,15)
    if x_test_mis_class_count :
        for i in range (4):
            for j in range (2):
                if count < mis_class_len :
                    ax[i,j].imshow(x_test_mis_class_count[count])            
                    ax[i,j].set_title(str(pred_digits_mis_class_count_pre_label[count])+
                                      "\n"+str(y_test_mis_class_count_actual_label[count]))
                    plt.tight_layout()
                count+=1

    # Plot heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(_confusion_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()



