# Data Handling

## raw

This contains your raw data (which you might want to add to your `.gitignore`) so that it doesn't show up on github. Github has a file size limit of 100 Mb, which isn't that much.

**Never** overwrite or modify the data here - you'll thank me later

## processed_data

This contains various checkpoints of the data you've made and is typically data derived from `raw`, but isn't quite ready for `modeling` just yet. I've historically used this to store the results of long-running processes that are not-quite ready for modeling. This helps me avoid needing to reconstruct the data every time

You don't need to store **every** change individually - use your best judgment.

## modeling_data

This folder contains any changes you might make to your data right before modeling. How does this differ from `processed`? `processed` might contain general purpose modifications for all models you might try, but this folder might contain model-specific changes.

E.g. you normalized your data for your linear regression, but you don't necessarily want to normalize the data for **all** your models. You might want to save the normalized data here as a "cache", especially if normalizing takes a long time. This will speed up turnaround time significantly.
