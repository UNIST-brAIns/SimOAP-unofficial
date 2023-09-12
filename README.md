# SimOAP-unofficial
Unofficial Implementation of [SimOAP: Improve Coherence and Consistency in Persona-based Dialogue Generation via Over-sampling and Post-evaluation](https://arxiv.org/abs/2305.11130)

# How to Use
## Fine-tuning
1. Download `pytorch_model.bin` from [DistilGPT2](https://huggingface.co/distilgpt2)
2. `git clone` or manually upload this repository to your Google Drive's base directory. (i.e. `/content/drive/MyDrive` in Google Colab)
3. Place downloaded `pytorch_model.bin` to `repo_name/gpt2-small/` directory.
4. Run our script on [Google Colab](https://colab.research.google.com/drive/1ewPbywzTG0130uXuBhkOu_vep839HRuC?usp=sharing)

## Evaluation


# TODOs
- [x] Oversampling
- [x] Coherence Evaluation
- [x] Consistecy Evaluation
- [x] distinct-1/2
- [x] sentence-level repetition rate
- [x] perplexity
- [ ] Implementation for BERT-over-BERT
- [ ] Merge Maximum Mutual Information (MMI) and Length-normalized Likelihood Score (LLS) to the evaluation code.
- [ ] seems like using distilGPT2 causes tensor shape related problems.
- [ ] does not provide functionality for resuming from the checkpoint.
- [ ] batch processing is not possible on inference time
