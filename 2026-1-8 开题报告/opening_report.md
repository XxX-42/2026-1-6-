---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
size: 16:9
math: mathjax
---

<style>
/* 全局字体 */
section { 
  font-size: 27px; 
  line-height: 1.6;
}

/* 标题样式 */
h2 { 
  color: #2563eb; 
  border-bottom: 2px solid #3b82f6;
  padding-bottom: 8px;
}

/* 导航栏样式 */
.nav {
  font-size: 18px;
  color: #64748b;
  text-align: center;
  margin-top: -30px;
  margin-bottom: 5px;
  padding: 4px 0;
  border-bottom: 1px solid #e2e8f0;
}
.nav .current {
  color: #2563eb;
  font-weight: bold;
}

/* 表格美化 */
table { 
  font-size: 22px; 
  border-collapse: collapse;
  width: 100%;
}
th { 
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  color: white;
  padding: 10px;
}
td { 
  padding: 8px 12px;
  border-bottom: 1px solid #e5e7eb;
}
tr:nth-child(even) { background: #f8fafc; }

/* 代码块 */
code { 
  font-size: 20px; 
  background: #e0e7ff;
  color: #1e40af;
  padding: 2px 6px;
  border-radius: 4px;
}
pre code {
  display: block;
  padding: 12px;
  background: #1e293b;
  color: #e2e8f0;
  border-radius: 8px;
}

/* 列表间距 */
li { margin-bottom: 6px; }

/* 强调文本 */
strong { color: #1e40af; }
</style>

![w:280|200](cuit_logo.png)

# 多模态情感分析模型的研究与应用

## 本科毕业设计开题报告

**成都信息工程大学计算机学院**

**答辩人**：梁嘉轩 &emsp; **指导老师**：冯翱

---

## 目录

<style scoped>
section { 
  font-size: 22px; 
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
}
h2 { margin-bottom: 20px; }

.toc-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding: 0 10px;
}

.toc-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.toc-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 30px rgba(0,0,0,0.12);
}

.card-header {
  padding: 12px 16px;
  color: white;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
}

.phase-1 .card-header { background: linear-gradient(135deg, #1e3a8a, #3b82f6); }
.phase-2 .card-header { background: linear-gradient(135deg, #1d4ed8, #60a5fa); }
.phase-3 .card-header { background: linear-gradient(135deg, #2563eb, #93c5fd); }
.phase-4 .card-header { background: linear-gradient(135deg, #3b82f6, #bfdbfe); }

.card-body {
  padding: 14px 16px;
  color: #334155;
  line-height: 1.5;
}

.toc-item {
  margin-bottom: 8px;
  display: flex;
  align-items: flex-start;
}

.toc-num {
  font-weight: bold;
  color: #2563eb;
  min-width: 24px;
}

.toc-text {
  flex: 1;
}

.toc-text b { color: #1e40af; }

.phase-icon {
  font-size: 24px;
  margin-bottom: 4px;
}
</style>

<div class="toc-grid">

<div class="toc-card phase-1">
  <div class="card-header">
    <div class="phase-icon">🎯</div>
    Phase 1: 为什么做
  </div>
  <div class="card-body">
    <div class="toc-item">
      <span class="toc-num">1.</span>
      <span class="toc-text">课题背景与意义</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">2.</span>
      <span class="toc-text">国内外研究现状</span>
    </div>
  </div>
</div>

<div class="toc-card phase-2">
  <div class="card-header">
    <div class="phase-icon">⚙️</div>
    Phase 2: 怎么做
  </div>
  <div class="card-body">
    <div class="toc-item">
      <span class="toc-num">3.</span>
      <span class="toc-text"><b>数据集介绍</b></span>
    </div>
    <div class="toc-item">
      <span class="toc-num">4.</span>
      <span class="toc-text"><b>核心技术路线</b></span>
    </div>
    <div class="toc-item">
      <span class="toc-num">5.</span>
      <span class="toc-text"><b>特征提取详解</b></span>
    </div>
  </div>
</div>

<div class="toc-card phase-3">
  <div class="card-header">
    <div class="phase-icon">🔬</div>
    Phase 3: 怎么验证
  </div>
  <div class="card-body">
    <div class="toc-item">
      <span class="toc-num">6.</span>
      <span class="toc-text"><b>融合机制与分类器</b></span>
    </div>
    <div class="toc-item">
      <span class="toc-num">7.</span>
      <span class="toc-text"><b>实验设计</b></span>
    </div>
  </div>
</div>

<div class="toc-card phase-4">
  <div class="card-header">
    <div class="phase-icon">📅</div>
    Phase 4: 何时做
  </div>
  <div class="card-body">
    <div class="toc-item">
      <span class="toc-num">8.</span>
      <span class="toc-text">预期产出与计划</span>
    </div>
  </div>
</div>

</div>

---

<div class="nav"><span class="current">1.背景</span> | 2.现状 | 3.数据集 | 4.技术 | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 1. 课题背景与意义

**研究背景：**
* 单模态方法难以准确识别反讽、双关等复杂情感表达
* 表情包与文字含义常存在矛盾，单一信息源易产生误判
* 短视频平台用户规模突破10亿，多模态数据成为主流
* 中文语境下的隐晦表达缺乏专用研究数据集

**研究意义：**
* **互补性**：文本语义、面部表情、声调韵律三通道相互印证
* **鲁棒性**：单一模态缺失或受噪声干扰时，其他模态可补充
* **应用前景**：舆情监控、智能客服、心理健康分析、人机交互

---

<div class="nav">1.背景 | <span class="current">2.现状</span> | 3.数据集 | 4.技术 | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 2. 国内外研究现状

**发展历程：**
* **早期**：简单拼接 (Early/Late Fusion)。
* **中期**：双流网络 + 注意力机制 (Attention)。
* **当前**：**Transformer & 大模型** (CLIP, ViT, BERT)。

**目前挑战：**
* 模态间的语义对齐（Alignment）。
* 异构数据的特征融合效率。
* **中文多模态数据集稀缺**。

---

<div class="nav">1.背景 | 2.现状 | <span class="current">3.数据集</span> | 4.技术 | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 3. 数据集介绍：CH-SIMS

**CH-SIMS**（Chinese Single- and Multi-modal Sentiment）是首个中文多模态情感数据集。

| 统计项     | 训练集 (Train) | 验证集 (Val) | 测试集 (Test) | **总计**  |
| :--------- | :------------: | :----------: | :-----------: | :-------: |
| **样本数** |     1,368      |     456      |      457      | **2,281** |
| **比例**   |      60%       |     20%      |      20%      |   100%    |

**数据特性：**
* **来源**：电影、电视剧片段（非受控环境，含噪声）。
* **标注**：每一样本包含 `(Text, Visual, Audio, Multimodal)` 4个独立标签。
* **不平衡性**：正负样本分布不均，需在 Loss 计算时引入**类别权重 (Class Weights)**。

---

<div class="nav">1.背景 | 2.现状 | <span class="current">3.数据集</span> | 4.技术 | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 3.1 数据挑战与预处理策略

**核心挑战**：CH-SIMS 属"野外"数据，**48.97% 的样本存在模态情感冲突** (Modality Incongruence)，且含大量背景噪声。

**预处理流水线 (Pipeline)**：

| 阶段     | 关键操作                                | 目的与依据                        |
| :------- | :-------------------------------------- | :-------------------------------- |
| **清洗** | 剔除 `Missing Modality` 及极短片段      | 保证三模态时序完整性              |
| **对齐** | **Word-level Alignment** (基于MMSA标准) | 解决音画不同步，统一采样率        |
| **视觉** | **MTCNN** 人脸检测与矫正                | 消除头部姿态差异 (Pose Invariant) |
| **声学** | **OpenSMILE** (IS10 特征集)             | 捕获语调、重音等副语言特征        |

> **注**：为应对复杂噪声，本项目基于 MMSA 框架复现特征提取流程，而非简单加载预制文件，以确保对原始数据的完全掌控。

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | <span class="current">4.技术</span> | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 4. 核心技术路线：三塔架构

![h:450](three_tower_arch.png)

---

<!-- _class: lead -->
<!-- _paginate: false -->

<style scoped>
section {
  padding: 0 !important;
  margin: 0 !important;
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  margin-top: -1px;
  margin-bottom: -5px;
}
</style>

![h:720](three_tower_arch.png)

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | <span class="current">4.技术</span> | 5.特征 | 6.融合 | 7.实验 | 8.产出</div>

## 4.1 工程可行性

**硬件约束**：RTX 3060 Laptop (6GB VRAM) vs **三塔模型高显存需求**。

**解决方案：空间换时间 + 梯度累积**

1.  **Stage 1: 离线特征提取 (Freeze & Extract)**
    * 使用预训练模型 (BERT/ResNet) 将原始多媒体流转化为低维向量存储 (Disk I/O)。
    * **效果**：训练阶段显存占用降低 **60%-70%**。

2.  **Stage 2: 梯度累积 (Gradient Accumulation)**
    * 设置 `Batch Size = 1`，`Accumulation Steps = 32`。
    * **数学等价性**：在数学期望上等价于 `Batch Size = 32` 的训练效果，保证 BN 层统计稳定性。

3.  **Stage 3: 混合精度训练 (AMP)**
    * 启用 FP16 精度，显存占用减半，利用 Tensor Core 加速。

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | <span class="current">5.特征</span> | 6.融合 | 7.实验 | 8.产出</div>

## 5. 特征提取详解：文本塔

**模型**：`bert-base-chinese`

**处理流程**：
1. 分词：使用 `BertTokenizer` 处理中文文本
2. 编码：输入 BERT 获取隐藏状态
3. 取特征：`[CLS]` token → $T \in \mathbb{R}^{768}$

```python
# 伪代码示例
output = bert_model(input_ids, attention_mask)
text_feat = output.last_hidden_state[:, 0, :]  # [CLS]
```

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | <span class="current">5.特征</span> | 6.融合 | 7.实验 | 8.产出</div>

## 5.1 视觉塔关键技术：人脸仿射变换

**问题**：影视剧场景中人物存在大量侧脸、旋转、遮挡，直接输入 CNN 会引入姿态噪声。

**解决方案：基于 5 关键点的仿射变换 (Affine Transformation)**

1.  **Landmark Detection**: 使用 MTCNN 定位 [左眼, 右眼, 鼻尖, 左嘴, 右嘴]。
2.  **Geometric Alignment**: 计算变换矩阵 $M$，将五官映射到标准正脸坐标系。
3.  **Feature Extraction**: 仅将校正后的 112x112 区域输入 ResNet-50。

$$
\text{Face}_{aligned} = \text{Affine}(\text{Image}_{raw}, \text{Landmarks}_{5pts})
$$

**作用**：解耦"姿态"与"表情"，让模型专注于**微表情 (Micro-expression)** 特征。

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | <span class="current">5.特征</span> | 6.融合 | 7.实验 | 8.产出</div>

## 5.2 视觉塔处理流程

**流程**：
1. **人脸检测**：MTCNN 检测并定位 5 关键点
2. **仿射对齐**：基于关键点进行仿射变换，归一化至 224×224
3. **特征提取**：ResNet-50（ImageNet 预训练）
4. **时序聚合**：Mean Pooling over frames

$$
V = \frac{1}{N}\sum_{i=1}^{N} \text{ResNet}(\text{Align}(f_i)) \in \mathbb{R}^{2048}
$$

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | <span class="current">5.特征</span> | 6.融合 | 7.实验 | 8.产出</div>

## 5.3 特征提取详解：声学塔

**工具链**：OpenSMILE / Librosa

**特征类型**：
- **MFCC**（13维）：捕捉频谱包络
- **Chroma**（12维）：音高分布
- **Spectral Contrast**（7维）：频谱对比度

**编码器**：Conv1D (Kernel=3, Stride=1, Channels=128)

$$
A = \text{MeanPool}(\text{Conv1D}(\text{Features})) \in \mathbb{R}^{256}
$$

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | 5.特征 | <span class="current">6.融合</span> | 7.实验 | 8.产出</div>

## 6. 融合机制：特征级融合 (Feature-level Fusion)

**架构选择**：鉴于 Late Fusion 丢失交互信息，Early Fusion 维度爆炸，采用 **Feature-level Fusion**。

**融合公式**：
$$
\mathbf{h}_{m} = \text{Concat}(\mathbf{h}_{text}, \mathbf{h}_{visual}, \mathbf{h}_{audio}) \in \mathbb{R}^{d_{total}}
$$

**分类器设计 (MLP Head)**：
* **Layer 1**: Linear ($d_{total} \to 128$) + ReLU + **Dropout (0.5)** (防止过拟合)
* **Layer 2**: Linear ($128 \to 3$) + Softmax
* **Loss Function**: Weighted Cross-Entropy (解决样本不平衡)

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | 5.特征 | 6.融合 | <span class="current">7.实验</span> | 8.产出</div>

## 7. 实验设计：验证指标与消融分析

**核心假设**：$\text{Acc}_{\text{Full}} > \max(\text{Acc}_T, \text{Acc}_V, \text{Acc}_A)$ (多模态互补性)

**评价指标 (Metrics)**：
* **Weighted F1-Score**：**核心指标**。鉴于 CH-SIMS 存在类别不平衡，Accuracy 存在虚高风险，F1 更具参考价值。
* **Accuracy-2 / Accuracy-3**：辅助指标。

**消融实验 (Ablation Study) 计划**：

| 实验组         | 模态组合         | 目的                              |
| :------------- | :--------------- | :-------------------------------- |
| **Unimodal**   | T / V / A        | 确立单模态基线 (特别是 Text-only) |
| **Bimodal**    | T+V / T+A / V+A  | 探究视觉与声学哪个对文本补充更强  |
| **Multimodal** | **T+V+A (Full)** | 验证三塔架构的完整增益            |

---

<div class="nav">1.背景 | 2.现状 | 3.数据集 | 4.技术 | 5.特征 | 6.融合 | 7.实验 | <span class="current">8.产出</span></div>

## 8. 预期产出与计划

<style scoped>section { font-size: 23px; } table { font-size: 20px; } li { margin-bottom: 2px; }</style>

**预期产出：**
* 完整的多模态情感分析模型源码（PyTorch）
*  一个系统演示界面
* 毕业设计论文一篇
* 实验对比数据报告（含消融实验）

**进度安排：**
| 阶段     | 时间  | 任务                     |
| -------- | ----- | ------------------------ |
| 数据准备 | 1-2月 | CH-SIMS 预处理与特征提取 |
| 模型搭建 | 3月   | 三塔架构实现与初步训练   |
| 实验调优 | 4月   | 参数调优与消融实验       |
| 论文撰写 | 5月   | 论文撰写与答辩准备       |

---

## 参考文献 (References)

<style scoped>section { font-size: 21px; }</style>

1. **[CH-SIMS]** Yu, W., Xu, H., et al. "CH-SIMS: A Chinese Multimodal Sentiment Analysis Dataset with Fine-grained Annotation of Modality." *ACL 2020*.
2. **[BERT]** Devlin, J., et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *NAACL 2019*.
3. **[ResNet]** He, K., et al. "Deep Residual Learning for Image Recognition." *CVPR 2016*.
4. **[OpenSMILE]** Eyben, F., et al. "openSMILE: the Munich versatile and fast open-source audio feature extractor." *ACM MM 2010*.
5. **[Multimodal Survey]** Poria, S., et al. "Multimodal sentiment analysis: A generic review." *IEEE Intelligent Systems, 2017*.

---

![w:200|200](cuit_logo.png)

## 请各位老师批评指正

**成都信息工程大学计算机学院**