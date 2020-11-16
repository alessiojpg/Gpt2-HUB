#!/usr/bin/env python
# coding=utf-8

#---------------------------- UTILITIES ----------------------------
import os
import sys
import json
from datetime import datetime
import shutil

os.chdir(sys.path[0])

def cls(): print ("\n" * 70)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#---------------------------- UTILITIES ----------------------------

def conditional_samples():
    os.chdir(sys.path[0])
    cls()

    with open('config/config.json', 'r') as f:
        config = json.load(f)

    def cond_menu( ):
        print(bcolors.OKBLUE + bcolors.BOLD + "\n~~ INTERACTIVE CONDITIONAL SAMPLES .py~~\n\n" + bcolors.ENDC + bcolors.ENDC +
              bcolors.UNDERLINE + "parametri:\n" + bcolors.ENDC +
              "(1) - Model name: " + bcolors.BOLD + str(config['model_name']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(2) - Seed: " + bcolors.BOLD + str(config['seed']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(3) - Number of samples: " + bcolors.BOLD + str(config['nsamples']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(4) - Batch size: " + bcolors.BOLD + str(config['batch_size']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(5) - Lenght: " + bcolors.BOLD + str(config['length']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(6) - Temperature: " + bcolors.BOLD + str(config['temperature']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(7) - Top K: " + bcolors.BOLD + str(config['top_k']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n" +
              "(8) - Top P: " + bcolors.BOLD + str(config['top_p']).strip('(').strip(')').strip(',').strip("'") + bcolors.ENDC + "\n\n" +

              bcolors.BOLD + "[ENTER] - RUN\n\n" + bcolors.ENDC +
              "(D) - DEFAULT SETTINGS\n" +
              "(H) - HELP\n" +
              "(M) - BACK TO MENU\n"
              + bcolors.FAIL + bcolors.BOLD + "[X] - EXIT" + bcolors.ENDC + bcolors.ENDC + "\n")

        start = input(">> ")

        if start == str(1):
            print('\n' + bcolors.BOLD + "String" + bcolors.ENDC + " - " + bcolors.OKGREEN + "which model to use" + bcolors.ENDC + '\n')
            modelsfiles = os.listdir("./gpt-2/models")
            if '.DS_Store' in modelsfiles:
                modelsfiles.remove('.DS_Store')
            else:
                pass
            print(bcolors.UNDERLINE + "Modelli disponibili:" + bcolors.ENDC)

            n = 1
            diz = {}

            for i in modelsfiles:
                print(str(n) + ' - ' + i)
                diz[str(n)] = str(i)
                n += 1

            print('\n')
            modelname = input(">> ")

            new_model_name = str(diz[modelname])

            config['model_name'] = new_model_name

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(2):
            print('\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "seed for random number generators, fix seed to reproduce results" + bcolors.ENDC + '\n')
            new_seed = input(">> [0 = None] ")

            if int(new_seed) == 0:
                config['seed'] = 'None'
            else:
                config['seed'] = int(new_seed)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(3):
            print('\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of samples to return total" + bcolors.ENDC + '\n')
            new_samples = input(">> ")

            config['nsamples'] = int(new_samples)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(4):
            print('\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of batches (only affects speed/memory).  Must divide nsamples." + bcolors.ENDC + '\n')
            new_batch = input(">> ")

            config['batch_size'] = int(new_batch)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(5):
            print('\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of tokens in generated text, if None (default), is determined by model hyperparameters" + bcolors.ENDC + '\n')
            new_lenght = input(">> [0 = None] ")

            if int(new_lenght) == 0:
                config['length'] = 'None'
            else:
                config['length'] = int(new_lenght)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(6):
            print('\n' + bcolors.BOLD + "Float" + bcolors.ENDC + " - " + bcolors.OKGREEN + "value controlling randomness in boltzmann distribution. \n"
                                                                                           "Lower temperature results in less random completions. \nt"
                                                                                           "As the temperature approaches zero, the model will become deterministic and\n"
                                                                                           "repetitive. Higher temperature results in more random completions." + bcolors.ENDC + '\n')
            new_temp = input(">> ")

            config['temperature'] = float(new_temp)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(7):
            print('\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "value controlling diversity.\n"
                                                                                             "1 means only 1 word is considered for each step (token), resulting in deterministic completions,\n"
                                                                                             "while 40 means 40 words are considered at each step.\n"
                                                                                             "0 (default) is a special setting meaning no restrictions.\n"
                                                                                             "40 generally is a good value." + bcolors.ENDC + '\n')
            new_k = input(">> ")

            config['top_k'] = int(new_k)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(8):
            print('\n' + bcolors.BOLD + "Float" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Float value controlling diversity.\n"
                                                                                           "Implements nucleus sampling, overriding top_k\n"
                                                                                           "if set to a value > 0. A good setting is 0.9." + bcolors.ENDC + '\n')
            new_p = input(">> ")

            config['top_p'] = float(new_p)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == 'H' or start == 'h':
            help = """\n-model_name=117M : String, which model to use
-seed=None : Integer seed for random number generators, fix seed to reproduce results
-nsamples=1 : Number of samples to return total
-batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
-length=None : Number of tokens in generated text, if None (default), is
 determined by model hyperparameters
-temperature=1 : Float value controlling randomness in boltzmann
 distribution. Lower temperature results in less random completions. As the
 temperature approaches zero, the model will become deterministic and
 repetitive. Higher temperature results in more random completions.
-top_k=0 : Integer value controlling diversity. 1 means only 1 word is
 considered for each step (token), resulting in deterministic completions,
 while 40 means 40 words are considered at each step. 0 (default) is a
 special setting meaning no restrictions. 40 generally is a good value.
-top_p=0.0 : Float value controlling diversity. Implements nucleus sampling,
 overriding top_k if set to a value > 0. A good setting is 0.9."""
            print(help)

            input(bcolors.BOLD + '\nPremere INVIO per tornare al menù' + bcolors.ENDC)
            cond_menu()
        elif start == 'M' or start == 'm':
            menu()
        elif start == 'D' or start == 'd':
            shutil.copy("config/default.json", "config/default_temp.json")
            shutil.move("config/default_temp.json", "config/config.json")
            print(bcolors.OKGREEN + '\nSETTINGS SET BACK TO DEFAULT' + bcolors.ENDC)
            menu()
        elif start == '' or start == '':
            print("\nDo you want to save the output to /output/conditional/ ?")
            save = input("Y / N >> ")
            if save == 'Y' or save == 'y':
                os.chdir(sys.path[0])
                os.chdir('gpt-2/')
                os.system('source ../venv/bin/activate && python src/interactive_conditional_samples.py --model_name ' + str(
                    config['model_name']) + ' --seed ' + str(config['seed']) + ' --nsamples ' + str(
                    config['nsamples']) + ' --batch_size ' + str(config['batch_size']) + ' --length ' + str(
                    config['length']) + ' --temperature ' + str(config['temperature']) + ' --top_k ' + str(
                    config['top_k']) + ' | tee ../output/conditional/' + str(config['model_name']) + str(
                    datetime.now().strftime("_%Yy-%mm-%dd_%Hh-%Mmin-%Ssec")) + '.txt')
            elif save == 'N' or save == 'n':
                os.chdir(sys.path[0])
                os.chdir('gpt-2/')
                os.system('source ../venv/bin/activate && python src/interactive_conditional_samples.py --model_name ' + str(
                    config['model_name']) + ' --seed ' + str(config['seed']) + ' --nsamples ' + str(
                    config['nsamples']) + ' --batch_size ' + str(config['batch_size']) + ' --length ' + str(
                    config['length']) + ' --temperature ' + str(config['temperature']) + ' --top_k ' + str(
                    config['top_k']))
            else:
                print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
                cond_menu()

            menu()
        elif start == 'X' or start == 'x':
            quit()
        else:
            print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
            cond_menu()

    cond_menu()

def unconditional_samples():
    os.chdir(sys.path[0])
    cls()

    with open('config/config.json', 'r') as f:
        config = json.load(f)

    def cond_menu():
        print(
            bcolors.OKBLUE + bcolors.BOLD + "\n~~ GENERATE UNCONDITIONAL SAMPLES .py ~~\n\n" + bcolors.ENDC + bcolors.ENDC +
            bcolors.UNDERLINE + "parametri:\n" + bcolors.ENDC +
            "(1) - Model name: " + bcolors.BOLD + str(config['model_name']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(2) - Seed: " + bcolors.BOLD + str(config['seed']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(3) - Number of samples: " + bcolors.BOLD + str(config['nsamples']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(4) - Batch size: " + bcolors.BOLD + str(config['batch_size']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(5) - Lenght: " + bcolors.BOLD + str(config['length']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(6) - Temperature: " + bcolors.BOLD + str(config['temperature']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(7) - Top K: " + bcolors.BOLD + str(config['top_k']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n" +
            "(8) - Top P: " + bcolors.BOLD + str(config['top_p']).strip('(').strip(')').strip(',').strip(
                "'") + bcolors.ENDC + "\n\n" +

            bcolors.BOLD + "[ENTER] - RUN\n\n" + bcolors.ENDC +
            "(D) - DEFAULT SETTINGS\n" +
            "(H) - HELP\n" +
            "(M) - BACK TO MENU\n"
            + bcolors.FAIL + bcolors.BOLD + "[X] - EXIT" + bcolors.ENDC + bcolors.ENDC + "\n")

        start = input(">> ")

        if start == str(1):
            print(
                '\n' + bcolors.BOLD + "String" + bcolors.ENDC + " - " + bcolors.OKGREEN + "which model to use" + bcolors.ENDC + '\n')
            modelsfiles = os.listdir("./gpt-2/models")
            if '.DS_Store' in modelsfiles:
                modelsfiles.remove('.DS_Store')
            else:
                pass
            print(bcolors.UNDERLINE + "Modelli disponibili:" + bcolors.ENDC)

            n = 1
            diz = {}

            for i in modelsfiles:
                print(str(n) + ' - ' + i)
                diz[str(n)] = str(i)
                n += 1

            print('\n')
            modelname = input(">> ")

            new_model_name = str(diz[modelname])

            config['model_name'] = new_model_name

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(2):
            print(
                '\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "seed for random number generators, fix seed to reproduce results" + bcolors.ENDC + '\n')
            new_seed = input(">> [0 = None] ")

            if int(new_seed) == 0:
                config['seed'] = 'None'
            else:
                config['seed'] = int(new_seed)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(3):
            print(
                '\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of samples to return total" + bcolors.ENDC + '\n')
            new_samples = input(">> ")

            config['nsamples'] = int(new_samples)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(4):
            print(
                '\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of batches (only affects speed/memory).  Must divide nsamples." + bcolors.ENDC + '\n')
            new_batch = input(">> ")

            config['batch_size'] = int(new_batch)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(5):
            print(
                '\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Number of tokens in generated text, if None (default), is determined by model hyperparameters" + bcolors.ENDC + '\n')
            new_lenght = input(">> [0 = None] ")

            if int(new_lenght) == 0:
                config['length'] = 'None'
            else:
                config['length'] = int(new_lenght)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(6):
            print(
                '\n' + bcolors.BOLD + "Float" + bcolors.ENDC + " - " + bcolors.OKGREEN + "value controlling randomness in boltzmann distribution. \n"
                                                                                         "Lower temperature results in less random completions. \nt"
                                                                                         "As the temperature approaches zero, the model will become deterministic and\n"
                                                                                         "repetitive. Higher temperature results in more random completions." + bcolors.ENDC + '\n')
            new_temp = input(">> ")

            config['temperature'] = float(new_temp)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(7):
            print(
                '\n' + bcolors.BOLD + "Integer" + bcolors.ENDC + " - " + bcolors.OKGREEN + "value controlling diversity.\n"
                                                                                           "1 means only 1 word is considered for each step (token), resulting in deterministic completions,\n"
                                                                                           "while 40 means 40 words are considered at each step.\n"
                                                                                           "0 (default) is a special setting meaning no restrictions.\n"
                                                                                           "40 generally is a good value." + bcolors.ENDC + '\n')
            new_k = input(">> ")

            config['top_k'] = int(new_k)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == str(8):
            print(
                '\n' + bcolors.BOLD + "Float" + bcolors.ENDC + " - " + bcolors.OKGREEN + "Float value controlling diversity.\n"
                                                                                         "Implements nucleus sampling, overriding top_k\n"
                                                                                         "if set to a value > 0. A good setting is 0.9." + bcolors.ENDC + '\n')
            new_p = input(">> ")

            config['top_p'] = float(new_p)

            with open('config/config.json', 'w') as f:
                json.dump(config, f)

            cond_menu()
        elif start == 'H' or start == 'h':
            help = """\n-model_name=117M : String, which model to use
    -seed=None : Integer seed for random number generators, fix seed to reproduce results
    -nsamples=1 : Number of samples to return total
    -batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
    -length=None : Number of tokens in generated text, if None (default), is
     determined by model hyperparameters
    -temperature=1 : Float value controlling randomness in boltzmann
     distribution. Lower temperature results in less random completions. As the
     temperature approaches zero, the model will become deterministic and
     repetitive. Higher temperature results in more random completions.
    -top_k=0 : Integer value controlling diversity. 1 means only 1 word is
     considered for each step (token), resulting in deterministic completions,
     while 40 means 40 words are considered at each step. 0 (default) is a
     special setting meaning no restrictions. 40 generally is a good value.
    -top_p=0.0 : Float value controlling diversity. Implements nucleus sampling,
     overriding top_k if set to a value > 0. A good setting is 0.9."""
            print(help)

            input(bcolors.BOLD + '\nPremere INVIO per tornare al menù' + bcolors.ENDC)
            cond_menu()
        elif start == 'D' or start == 'd':
            shutil.copy("config/default.json", "config/default_temp.json")
            shutil.move("config/default_temp.json", "config/config.json")
            print(bcolors.OKGREEN + '\nSETTINGS SET BACK TO DEFAULT' + bcolors.ENDC)
            menu()
        elif start == 'M' or start == 'm':
            menu()
        elif start == '' or start == '':
            print("\nDo you want to save the output to /output/unconditional/ ?")
            save = input("Y / N >> ")
            if save == 'Y' or save == 'y':
                os.chdir(sys.path[0])
                os.chdir('gpt-2/')
                os.system('source ../venv/bin/activate && python src/generate_unconditional_samples.py --model_name ' + str(
                    config['model_name']) + ' --seed ' + str(config['seed']) + ' --nsamples ' + str(
                    config['nsamples']) + ' --batch_size ' + str(config['batch_size']) + ' --length ' + str(
                    config['length']) + ' --temperature ' + str(config['temperature']) + ' --top_k ' + str(
                    config['top_k']) + ' | tee ../output/unconditional/' + str(config['model_name']) + str(
                    datetime.now().strftime("_%Yy-%mm-%dd_%Hh-%Mmin-%Ssec")) + '.txt')
            elif save == 'N' or save == 'n':
                os.chdir(sys.path[0])
                os.chdir('gpt-2/')
                os.system('source ../venv/bin/activate && python src/generate_unconditional_samples.py --model_name ' + str(
                    config['model_name']) + ' --seed ' + str(config['seed']) + ' --nsamples ' + str(
                    config['nsamples']) + ' --batch_size ' + str(config['batch_size']) + ' --length ' + str(
                    config['length']) + ' --temperature ' + str(config['temperature']) + ' --top_k ' + str(
                    config['top_k']))
            else:
                print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
                cond_menu()

            input(bcolors.BOLD + '\nPremere INVIO per tornare al menù' + bcolors.ENDC)
            menu()
        elif start == 'X' or start == 'x':
            quit()
        else:
            print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
            cond_menu()

    cond_menu()

def encode():
    os.chdir(sys.path[0])
    cls()

    if os.path.isdir("./data") == True:
        pass
    else:
        print("~~ creo /data/ ~~\n")
        os.makedirs("data")
        os.makedirs("data/txt")
        os.makedirs("data/npz")

    datafiles = os.listdir("./data/txt/")

    if '.DS_Store' in datafiles:
        datafiles.remove('.DS_Store')
    else:
        pass

    print("\nScegliere il file da elaborare: \n")
    n = 1
    diz = {}

    for i in datafiles:
        print(str(n) + ' - ' + i)
        diz[str(n)] = str(i)
        n += 1

    print("\n")
    file = input(">> ")
    print("\n")
    print("Inserire nome del dataset di output in formato npz [e.g file.npz]:")
    npz = input(os.getcwd() + "/data/npz/")
    print("\n")

    modelsfiles = os.listdir("gpt-2/models")
    if '.DS_Store' in modelsfiles:
        modelsfiles.remove('.DS_Store')
    else:
        pass

    print("Modelli disponibili:\n")

    j = 1
    diz_mod = {}

    for i in modelsfiles:
        print(str(j) + ' - ' + i)
        diz_mod[str(j)] = str(i)
        j += 1

    print('\n')
    modelname = input(">> ")
    os.chdir('gpt-2/')
    os.system('source ../venv/bin/activate && PYTHONPATH=src python3 encode.py ' + '../data/txt/' + str(diz[file]) + ' ../data/npz/' + str(npz) + ' --model_name ' + str(diz_mod[modelname]))

    menu()

def train():
    os.chdir(sys.path[0])
    cls()

    datafiles = os.listdir("data/npz")
    if '.DS_Store' in datafiles:
        datafiles.remove('.DS_Store')
    else:
        pass

    modelsfiles = os.listdir("gpt-2/models")
    if '.DS_Store' in modelsfiles:
        modelsfiles.remove('.DS_Store')
    else:
        pass

    print("\nScegliere il dataset npz da elaborare: \n")
    n = 1
    diz_npz = {}

    for i in datafiles:
        print(str(n) + ' - ' + i)
        diz_npz[str(n)] = str(i)
        n += 1

    print("\n")
    npz = input(">> ")
    print("\n")
    print("Modelli disponibili:\n")

    n = 1
    diz = {}

    for i in modelsfiles:
        print(str(n) + ' - ' + i)
        diz[str(n)] = str(i)
        n += 1

    print('\n')
    modelname = input(">> ")
    print("\nNumber of training iterations: \n")
    iterations = input(">> ")
    print("\nName of the directory in which to save the checkpoint [e.g. run1]: (write an existing path name to resume)\n")
    run = input("/checkpoint/")
    print("\nAdditional parameters: \n")
    print("""[--dataset PATH] [--model_name MODEL] [--combine CHARS]
                [--encoding ENCODING] [--batch_size SIZE] [--learning_rate LR]
                [--accumulate_gradients N] [--memory_saving_gradients]
                [--only_train_transformer_layers] [--optimizer OPTIMIZER]
                [--noise NOISE] [--top_k TOP_K] [--top_p TOP_P]
                [--restore_from RESTORE_FROM] [--run_name RUN_NAME]
                [--sample_every N] [--sample_length TOKENS] [--sample_num N]
                [--save_every N] [--val_dataset PATH] [--val_batch_size SIZE]
                [--val_batch_count N] [--val_every STEPS]
                [--n_iterations NUMBER OF ITERATIONS]\n\n""")
    additional = input("PYTHONPATH=src ./train.py --dataset ../data/npz/" + str(diz_npz[npz]) + ' --model_name ' + str(diz[modelname]) + ' --n_iterations ' + iterations + " --run_name " + str(run) + ' ')
    os.chdir(sys.path[0])
    os.chdir('gpt-2/')
    os.system('source ../venv/bin/activate && PYTHONPATH=src ./train.py --dataset ../data/npz/' + str(diz_npz[npz]) + ' --model_name ' + str(diz[modelname]) + ' --n_iterations ' + str(iterations) + " --run_name " + str(run) + ' ' + str(additional))

    def savemenu():
        print("\nDo you want to save the model to /models ?")
        save = input("Y / N >> ")
        if save == 'Y' or save == 'y':
            os.chdir(sys.path[0])
            checkpoint_files = os.listdir("gpt-2/checkpoint/" + str(run))
            if '.DS_Store' in checkpoint_files:
                checkpoint_files.remove('.DS_Store')
            else:
                pass

            shutil.copytree("gpt-2/models/" + str(diz[modelname]), "gpt-2/models/" + str(run))

            for i in checkpoint_files:
                shutil.move("gpt-2/checkpoint/" + str(run) + '/' + i, "gpt-2/models/" + str(run) + '/' + i)
            os.rmdir("gpt-2/checkpoint/" + str(run))

            input(bcolors.BOLD + '\nPROCESSO COMPLETATO - Premere INVIO per tornare al menù' + bcolors.ENDC)

            menu()
        elif save == 'N' or save == 'n':
            input(bcolors.BOLD + '\nPROCESSO COMPLETATO - Premere INVIO per tornare al menù' + bcolors.ENDC)

            menu()
        else:
            print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
            savemenu()

    savemenu()

def list_models():
    os.chdir(sys.path[0])
    cls()

    modelsfiles = os.listdir("gpt-2/models")
    if '.DS_Store' in modelsfiles:
        modelsfiles.remove('.DS_Store')
    else:
        pass

    n = 1
    diz = {}

    print("\n")

    for i in modelsfiles:
        print(str(n) + ' - ' + i)
        diz[str(n)] = str(i)
        n += 1

    input(bcolors.BOLD + '\nPremere INVIO per tornare al menù' + bcolors.ENDC)
    menu()

def list_data():
    os.chdir(sys.path[0])
    cls()

    print(bcolors.BOLD + "\n~~ TXT ~~\n" + bcolors.ENDC)
    modelsfiles = os.listdir("data/txt")

    if '.DS_Store' in modelsfiles:
        modelsfiles.remove('.DS_Store')
    else:
        pass
    n = 1

    for i in modelsfiles:
        print(str(n) + ' - ' + i)
        n += 1

    print(bcolors.BOLD + "\n~~ NPZ ~~\n" + bcolors.ENDC)
    modelsfiles = os.listdir("data/npz")

    if '.DS_Store' in modelsfiles:
        modelsfiles.remove('.DS_Store')
    else:
        pass

    n = 1

    for i in modelsfiles:
        print(str(n) + ' - ' + i)
        n += 1

    input(bcolors.BOLD + '\nPremere INVIO per tornare al menù' + bcolors.ENDC)
    menu()

def helpf():
    menu()

def setup():
    os.chdir(sys.path[0])
    cls()

    print(bcolors.HEADER + bcolors.BOLD + "----- INIZIO SETUP -----\n" + bcolors.ENDC + bcolors.ENDC)

    print(bcolors.OKBLUE + "~~ creating directories ~~\n" + bcolors.ENDC)

    try:
        print("~~ creo /data/ ~~\n")
        os.makedirs("data")
        os.makedirs("data/txt")
        os.makedirs("data/npz")
    except:
        print("/data/ esiste già\n")

    try:
        print("~~ creo /output/ ~~\n")
        os.makedirs("output")
        os.makedirs("output/unconditional")
        os.makedirs("output/conditional")
    except:
        print("/output/ esiste già\n")

    print(bcolors.OKBLUE + "~~ set-up virtualenv ~~\n" + bcolors.ENDC)
    input(bcolors.BOLD + '\nPremere INVIO per continutare' + bcolors.ENDC)

    import platform
    if str(platform.system()) == 'Windows':
        os.system(r'py -m pip install --upgrade pip && py -m pip install --user virtualenv && py -m venv venv && .\venv\Scripts\activate')
    elif str(platform.system()) == 'Linux' or str(platform.system()) == 'Darwin':
        os.system('python3 -m pip install --upgrade pip && python3 -m pip install --user virtualenv && python3 -m venv venv && source venv/bin/activate')
    else:
        pass

    print(bcolors.OKBLUE + "~~ clonazione repository gpt-2 ~~\n" + bcolors.ENDC)
    input(bcolors.BOLD + '\nPremere INVIO per continutare' + bcolors.ENDC)

    os.system('git clone https://github.com/alessiojpg/gpt-2-MOD.git gpt-2')
    os.chdir('gpt-2')
    print(bcolors.OKBLUE + "~~ installo tensorflow 1.12 ~~\n" + bcolors.ENDC)
    if str(platform.system()) == 'Windows':
        os.system(r'..\venv\Scripts\activate && pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl && deactivate')
    elif str(platform.system()) == 'Linux':
        os.system('source ../venv/bin/activate && pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl && deactivate')
    elif str(platform.system()) == 'Darwin':
        os.system('source ../venv/bin/activate && pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl && deactivate')
    else:
        pass

    print(bcolors.OKBLUE + "~~ installo requirements ~~\n" + bcolors.ENDC)
    input(bcolors.BOLD + '\nPremere INVIO per continutare' + bcolors.ENDC)

    if str(platform.system()) == 'Windows':
        os.system(r'..\venv\Scripts\activate && pip3 install -r requirements.txt && deactivate')
    elif str(platform.system()) == 'Linux':
        os.system('source ../venv/bin/activate && pip3 install -r requirements.txt && deactivate')
    elif str(platform.system()) == 'Darwin':
        os.system('source ../venv/bin/activate && pip3 install -r requirements.txt && deactivate')
    else:
        pass


    def modelmenu():
        print(bcolors.FAIL + "Quale Model scaricare?" + bcolors.ENDC + "\n\n(1) - 124M\n(2) - 355M\n(3) - 774M\n(4) - 1558M\n\n")
        model = input('>> ')
        if model == str(1):
            if str(platform.system()) == 'Windows':
                os.system('py download_model.py 124M')
            elif str(platform.system()) == 'Linux':
                os.system('python3 download_model.py 124M')
            elif str(platform.system()) == 'Darwin':
                os.system('python3 download_model.py 124M')
            else:
                pass
        elif model == str(2):
            if str(platform.system()) == 'Windows':
                os.system('py download_model.py 355M')
            elif str(platform.system()) == 'Linux':
                os.system('python3 download_model.py 355M')
            elif str(platform.system()) == 'Darwin':
                os.system('python3 download_model.py 355M')
            else:
                pass
        elif model == str(3):
            if str(platform.system()) == 'Windows':
                os.system('py download_model.py 774M')
            elif str(platform.system()) == 'Linux':
                os.system('python3 download_model.py 774M')
            elif str(platform.system()) == 'Darwin':
                os.system('python3 download_model.py 774M')
            else:
                pass
        elif model == str(4):
            if str(platform.system()) == 'Windows':
                os.system('py download_model.py 1558M')
            elif str(platform.system()) == 'Linux':
                os.system('python3 download_model.py 1558M')
            elif str(platform.system()) == 'Darwin':
                os.system('python3 download_model.py 1558M')
            else:
                pass
        else:
            print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
            modelmenu()

    modelmenu()

    os.system('export PYTHONIOENCODING=UTF-8')

    os.chdir(sys.path[0])
    print(bcolors.HEADER + bcolors.BOLD + "----- SETUP COMPLETATO -----\n" + bcolors.ENDC + bcolors.ENDC)
    menu()

def clear():
    os.chdir(sys.path[0])
    cls()

    print(bcolors.WARNING + bcolors.BOLD + "\n[BE CAREFUL THIS WILL WIPE ALL OF GPT2'S DATA]\n\n" + bcolors.ENDC + bcolors.ENDC)
    yesno = input("Do you want to proceed? [YES (Y) / NO (n): ")

    if yesno == 'Y':
        print(bcolors.HEADER + bcolors.BOLD + "----- INIZIO PULIZIA -----\n" + bcolors.ENDC + bcolors.ENDC)
        print(bcolors.OKBLUE + "~~ elimino cartelle ~~\n" + bcolors.ENDC)
        import platform

        if str(platform.system()) == 'Windows':
            os.system('del /f /s /q gpt-2 1>nul')
            os.system('rmdir /s /q gpt-2')

            os.system('del /f /s /q venv 1>nul')
            os.system('rmdir /s /q venv')

            os.system('del /f /s /q data 1>nul')
            os.system('rmdir /s /q data')
        elif str(platform.system()) == 'Linux' or str(platform.system()) == 'Darwin':
            os.system('rm -r gpt-2')
            os.system('rm -r venv')
            os.system('rm -r data')
        else:
            print("ERROR")
        print(bcolors.OKBLUE + "~~ disinstallo tensorflow 1.12 ~~\n" + bcolors.ENDC)
        os.system('pip3 uninstall tensorflow')
        print(bcolors.OKBLUE + "~~ disinstallo requirements ~~\n" + bcolors.ENDC)
        os.system('pip3 uninstall -r requirements.txt')

        os.chdir(sys.path[0])
        print(bcolors.HEADER + bcolors.BOLD + "----- PULIZIA COMPLETATA -----\n" + bcolors.ENDC + bcolors.ENDC)
        menu()
    elif yesno == 'n' or yesno == 'N':
        print('\n')
        menu()
    else:
        print('Choose a valid option!\n')
        clear()

def advanced():
    os.chdir(sys.path[0])
    cls()

    print(bcolors.BOLD + bcolors.WARNING + "\nIMPOSTAZIONI AVANZATE:\n\n" + bcolors.ENDC + bcolors.ENDC +
          "(S) - SETUP\n"
          "(U) - WIPE ALL DATA\n\n"
          "(M) - BACK TO MENU\n"
          + bcolors.FAIL + bcolors.BOLD + "[X] - EXIT" + bcolors.ENDC + bcolors.ENDC + "\n")

    start = input(">> ")

    if start == str(1):
        conditional_samples()
    elif start == 'M' or start == 'm':
        menu()
    elif start == 'S' or start == 's':
        setup()
    elif start == 'U' or start == 'u':
        clear()
    elif start == 'X' or start == 'x':
        quit()
    else:
        print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
        advanced()

def modelmenu():
    os.chdir(sys.path[0])
    cls()

    os.chdir('gpt-2')
    print(bcolors.FAIL + "Quale Model scaricare?" + bcolors.ENDC + "\n\n(1) - 124M\n(2) - 355M\n(3) - 774M\n(4) - 1558M\n\n(M) - BACK TO MENU\n")
    model = input('>> ')
    if model == str(1):
        os.system('python3 download_model.py 124M')
        menu()
    elif model == str(2):
        os.system('python3 download_model.py 355M')
        menu()
    elif model == str(3):
        os.system('python3 download_model.py 774M')
        menu()
    elif model == str(4):
        os.system('python3 download_model.py 1558M')
        menu()
    elif model == 'M' or model == 'm':
        menu()
    else:
        print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
        modelmenu()

def menu():
    os.chdir(sys.path[0])

    cls()

    print(bcolors.BOLD + "\nBENVENUTO IN GPT-2!\n\n" + bcolors.ENDC +
          bcolors.UNDERLINE + "OPZIONI:\n\n" + bcolors.ENDC +
          "--Funzioni:\n"
          "(1) - Genera testo con prompt.\n(2) - Genera testo incondizionato.\n(3) - Encode dataset.\n(4) - Train model.\n\n"
          "--utility:\n"
          "(5) - Lista modelli disponibili.\n(6) - /data\n(7) - /Download models\n\n"
          "--tools:\n"
          "(8) - Webscraper.\n(9) - WIKIscraper\n\n"
          "--altro:\n"
          "(S) - SETUP / INITIALIZE\n(H) - HELP\n" +
          "(A) - ADVANCED OPTIONS\n\n"
          + bcolors.FAIL + bcolors.BOLD +  "[X] - EXIT" + bcolors.ENDC + bcolors.ENDC + "\n")

    start = input(">> ")

    if start == str(1):
        conditional_samples()
    elif start == str(2):
        unconditional_samples()
    elif start == str(3):
        encode()
    elif start == str(4):
        train()
    elif start == str(5):
        list_models()
    elif start == str(6):
        list_data()
    elif start == str(7):
        modelmenu()
    elif start == str(8):
        os.system('python webscraper.py')
    elif start == str(9):
        os.system('python wikiscraper.py')
    elif start == str(6):
        pass
    elif start == str(6):
        pass
    elif start == str(6):
        pass
    elif start == str(7):
        pass
    elif start == 'H' or start == 'h':
        helpf()
    elif start == 'S' or start == 's':
        setup()
    elif start == 'A' or start == 'a':
        advanced()
    elif start == 'X' or start == 'x':
        quit()
    else:
        print(bcolors.WARNING + "Scegli un'opzione valida!" + bcolors.ENDC)
        menu()

try:
    try:
        os.system('source venv/bin/activate')
    except:
        os.system('.\env\Scripts\activate')
except:
    print("You gotta SETUP")

menu()