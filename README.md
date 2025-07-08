<div align="center">
  <a href="https://github.com/antonio-backnotfront/linear-regression/stargazers">
    <img src="https://img.shields.io/github/stars/antonio-backnotfront/linear-regression?style=for-the-badge" alt="GitHub stars">
  </a>
  <a href="https://github.com/antonio-backnotfront/linear-regression/issues">
    <img src="https://img.shields.io/github/issues/antonio-backnotfront/linear-regression.svg?style=for-the-badge" alt="GitHub issues">
  </a>
  <a href="https://github.com/antonio-backnotfront/linear-regression/blob/main/LICENSE.txt">
    <img src="https://img.shields.io/github/license/antonio-backnotfront/linear-regression.svg?style=for-the-badge" alt="License">
  </a>
<br>
<a href="https://linkedin.com/in/anton-solianyk-906453221">
  <img src="https://img.shields.io/badge/🔗%20LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>

  <a href="mailto:solyanicks@gmail.com">
    <img src="https://img.shields.io/badge/Email-solyanicks%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</div>



<h1 align="center">🤖📈 Linear regression</h1>
<p align="center">An implementation of the fundamental Machine Learning Algorithm.</p>
<p align="center">The algorithm is implemented in two separate ways:</p>

<table align="center">
<tr>
<td valign="top">

<h3 align="center">🐍 Raw Python Version</h3>

<ul>
  <li>No external libraries</li>
  <li>Custom-built linear regression</li>
  <li>Ideal for learning math</li>
  <br>
</ul>

</td>
<td valign="top" width="60%">

<h3 align="center">🚀 Enhanced Version</h3>

<ul>
  <li>Uses <code>NumPy</code>, <code>Pandas</code>, <code>Matplotlib</code>, <code>PyTorch</code></li>
  <li>Faster, cleaner, and production-ready</li>
  <li>Great for experimentation & visualization</li>
</ul>

</td>
</tr>
</table>



<br/>
<p align="center">
  <a href="#-how-it-works" style="padding-right: 12px;"><strong>How It Works</strong></a> •
  <a href="#-when-it-works" style="padding-right: 12px;"><strong>When It Works</strong></a> •
  <a href="#-demo" style="padding-right: 12px;"><strong>Demo</strong></a> •
  <a href="#-usage" style="padding-right: 12px;"><strong>Usage</strong></a> •
  <a href="#-technologies-used" style="padding-right: 12px;"><strong>Tech</strong></a> •
  <a href="#-license" style="padding-right: 12px;"><strong>License</strong></a>
</p>

---

## 📝 How it works


![img](.github/images/linear-regression-pic.png)

So basically the whole model is represented by this slope, which is used to predict values.  
The prediction is based on parameters passed to the model ("x" on the slope), the "x" is not limited by one parameter, 
it may be a set of parameters.

### Training
The model is trained using the dataset in folder ```src/data``` using K-fold Cross-Validation technique.  
Before the actual training, the data is shuffled to guarantee a consistency.  
Cross-Validation works in the following way:  
take the dataset, split it into K roughly equal parts, use K-1 parts to train the data, use 1 remaining part
for testing (validation).


## 🧠 When It Works
## 📱 Demo
## 💻 Usage
## 📄 License
## ⚙️ Used Technologies

> One Parameter


$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$