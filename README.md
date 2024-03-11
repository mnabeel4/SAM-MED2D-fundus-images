SAM-MED2D for fundus images

## 👉 Framework
The pipeline of SAM-Med2D. We freeze the image encoder and incorporate learnable adapter layers in each Transformer block to acquire domain-specific knowledge in the medical field. We fine-tune the prompt encoder using point, Bbox, and mask information, while updating the parameters of the mask decoder through interactive training.
<p align="center"><img width="800" alt="image" src="https://github.com/OpenGVLab/SAM-Med2D/blob/main/assets/framwork.png"></p> 

## 👉 Results

<table>
  <caption align="center">Quantitative comparison of different methods on the test set: </caption>
  <thead>
    <tr>
      <th>Model</th>
      <th>Resolution</th>
      <th>Bbox (%)</th>
      <th>1 pt (%)</th>
      <th>3 pts (%)</th>
      <th>5 pts (%)</th>
      <th>FPS</th>
      <th>Checkpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">SAM</td>
      <td align="center">$256\times256$</td>
      <td align="center">61.63</td>
      <td align="center">18.94</td>
      <td align="center">28.28</td>
      <td align="center">37.47</td>
      <td align="center">51</td>
      <td align="center"><a href="https://drive.google.com/file/d/1_U26MIJhWnWVwmI5JkGg2cd2J6MvkqU-/view?usp=drive_link">Offical</a></td>
    </tr>
    <tr>
      <td align="center">SAM</td>
      <td align="center">$1024\times1024$</td>
      <td align="center">74.49</td>
      <td align="center">36.88</td>
      <td align="center">42.00</td>
      <td align="center">47.57</td>
      <td align="center">8</td>
      <td align="center"><a href="https://drive.google.com/file/d/1_U26MIJhWnWVwmI5JkGg2cd2J6MvkqU-/view?usp=drive_link">Offical</a></td>
    </tr>
    <tr>
      <td align="center">FT-SAM</td>
      <td align="center">$256\times256$</td>
      <td align="center">73.56</td>
      <td align="center">60.11</td>
      <td align="center">70.95</td>
      <td align="center">75.51</td>
      <td align="center">51</td>
      <td align="center"><a href="https://drive.google.com/file/d/1J4qQt9MZZYdv1eoxMTJ4FL8Fz65iUFM8/view?usp=drive_link">FT-SAM</a></td>
    </tr>
    <tr>
      <td align="center">SAM-Med2D</td>
      <td align="center">$256\times256$</td>
      <td align="center">79.30</td>
      <td align="center">70.01</td>
      <td align="center">76.35</td>
      <td align="center">78.68</td>
      <td align="center">35</td>
      <td align="center"><a href="https://drive.google.com/file/d/1ARiB5RkSsWmAB_8mqWnwDF8ZKTtFwsjl/view?usp=drive_link">SAM-Med2D</a></td>
    </tr>
  </tbody>
</table>


<table>
    <caption align="center">Generalization validation on 9 MICCAI2023 datasets, where "*" denotes that we drop adapter layer of SAM-Med2D in test phase: </caption>
  <thead>
    <tr>
      <th rowspan="2">Datasets</th>
      <th colspan="3">Bbox prompt (%)</th>
      <th colspan="3">1 point prompt (%)</th>
    </tr>
    <tr>
      <th>SAM</th>
      <th>SAM-Med2D</th>
      <th>SAM-Med2D*</th>
      <th>SAM</th>
      <th>SAM-Med2D</th>
      <th>SAM-Med2D*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.synapse.org/#!Synapse:syn51236108/wiki/621615">CrossMoDA23</a></td>
      <td align="center">78.98</td>
      <td align="center">70.51</td>
      <td align="center">84.62</td>
      <td align="center">18.49</td>
      <td align="center">46.08</td>
      <td align="center">73.98</td>
    </tr>
    <tr>
      <td align="center"><a href="https://kits-challenge.org/kits23/">KiTS23</a></td>
      <td align="center">84.80</td>
      <td align="center">76.32</td>
      <td align="center">87.93</td>
      <td align="center">38.93</td>
      <td align="center">48.81</td>
      <td align="center">79.87</td>
    </tr>
    <tr>
      <td align="center"><a href="https://codalab.lisn.upsaclay.fr/competitions/12239#learn_the_details">FLARE23</a></td>
      <td align="center">86.11</td>
      <td align="center">83.51</td>
      <td align="center">90.95</td>
      <td align="center">51.05</td>
      <td align="center">62.86</td>
      <td align="center">85.10</td>
    </tr>
    <tr>
      <td align="center"><a href="https://atlas-challenge.u-bourgogne.fr/">ATLAS2023</a></td>
      <td align="center">82.98</td>
      <td align="center">73.70</td>
      <td align="center">86.56</td>
      <td align="center">46.89</td>
      <td align="center">34.72</td>
      <td align="center">70.42</td>
    </tr>
    <tr>
      <td align="center"><a href="https://multicenteraorta.grand-challenge.org/">SEG2023</a></td>
      <td align="center">75.98</td>
      <td align="center">68.02</td>
      <td align="center">84.31</td>
      <td align="center">11.75</td>
      <td align="center">48.05</td>
      <td align="center">69.85</td>
    </tr>
    <tr>
      <td align="center"><a href="https://lnq2023.grand-challenge.org/lnq2023/">LNQ2023</a></td>
      <td align="center">72.31</td>
      <td align="center">63.84</td>
      <td align="center">81.33</td>
      <td align="center">3.81</td>
      <td align="center">44.81</td>
      <td align="center">59.84</td>
    </tr>
    <tr>
      <td align="center"><a href="https://codalab.lisn.upsaclay.fr/competitions/9804">CAS2023</a></td>
      <td align="center">52.34</td>
      <td align="center">46.11</td>
      <td align="center">60.38</td>
      <td align="center">0.45</td>
      <td align="center">28.79</td>
      <td align="center">15.19</td>
    </tr>
    <tr>
      <td align="center"><a href="https://tdsc-abus2023.grand-challenge.org/Dataset/">TDSC-ABUS2023</a></td>
      <td align="center">71.66</td>
      <td align="center">64.65</td>
      <td align="center">76.65</td>
      <td align="center">12.11</td>
      <td align="center">35.99</td>
      <td align="center">61.84</td>
    </tr>
    <tr>
      <td align="center"><a href="https://toothfairy.grand-challenge.org/toothfairy/">ToothFairy2023</a></td>
      <td align="center">65.86</td>
      <td align="center">57.45</td>
      <td align="center">75.29</td>
      <td align="center">1.01</td>
      <td align="center">32.12</td>
      <td align="center">47.32</td>
    </tr>
    <tr>
      <td align="center">Weighted sum</td>
      <td align="center">85.35</td>
      <td align="center">81.93</td>
      <td align="center">90.12</td>
      <td align="center">48.08</td>
      <td align="center">60.31</td>
      <td align="center">83.41</td>
    </tr>
  </tbody>
</table>


## 👉 Visualization
<p align="center"><img width="800" alt="image" src="https://github.com/OpenGVLab/SAM-Med2D/blob/main/assets/visualization.png"></p> 

## 👉 Test
Prepare your own dataset and refer to the samples in `SAM-Med2D/data_demo` to replace them according to your specific scenario. You need to generate the "label2image_test.json" file before running "test.py"

```bash
cd ./SAM-Med2d
python test.py
```
- work_dir: Specifies the working directory for the testing process. Default value is "workdir".
- batch_size: 1.
- image_size: Default value is 256.
- boxes_prompt: Use Bbox prompt to get segmentation results. 
- point_num: Specifies the number of points. Default value is 1.
- iter_point: Specifies the number of iterations for point prompts.
- sam_checkpoint: Load sam or sammed checkpoint.
- encoder_adapter: Set to True if using SAM-Med2D's pretrained weights.
- save_pred: Whether to save the prediction results.
- prompt_path: Is there a fixed Prompt file? If not, the value is None, and it will be automatically generated in the latest prediction.

## 👉 Deploy

### Export to ONNX

- export encoder model

```bash
python3 scripts/export_onnx_encoder_model.py --sam_checkpoint /path/to/sam-med2d_b.pth --output /path/to/sam-med2d_b.encoder.onnx --model-type vit_b --image_size 256 --encoder_adapter True
```

- export decoder model

```bash
python3 scripts/export_onnx_model.py --checkpoint /path/to/sam-med2d_b.pth --output /path/to/sam-med2d_b.decoder.onnx --model-type vit_b --return-single-mask
```

- inference with onnxruntime

```
# cd examples/SAM-Med2D-onnxruntime
python3 main.py --encoder_model /path/to/sam-med2d_b.encoder.onnx --decoder_model /path/to/sam-med2d_b.decoder.onnx


