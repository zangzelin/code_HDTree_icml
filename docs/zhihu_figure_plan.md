# HDTree 知乎图文设计

## 推荐主图组合

### 图 1：Motivation

文件：

```text
docs/assets/zhihu/fig1_motivation.png
```

放置位置：文章开头之后，进入“为什么普通 clustering 不够？”之前。

作用：快速解释 HDTree 相比传统层次聚类和 branch-specific deep tree models 的动机，包括稳定性、生成能力、准确性和训练成本。

知乎图注：

> HDTree 的问题动机。传统层次聚类缺少生成能力，branch-specific deep tree models 稳定性和扩展性受限；HDTree 用统一模型同时建模层次结构和生成过程。

### 图 2：Method Overview

文件：

```text
docs/assets/zhihu/fig2_hdtree_framework.png
```

放置位置：“HDTree 的核心想法”小节后。

作用：解释模型结构，包括 Encoder、Hierarchical Tree Codebook、Diffusion Decoder 和 Lineage Analysis。它是全文最关键的一张方法图。

知乎图注：

> HDTree 方法总览。模型由 encoder、Hierarchical Tree Codebook 和 diffusion decoder 组成，并基于 learned tree 进行 lineage analysis。

### 图 3：Lineage Case Study

文件：

```text
docs/assets/zhihu/fig3_lineage_case_study.png
```

放置位置：“Lineage ground truth：学到的路径是否符合发育时间？”小节后。

作用：展示 TreeVAE 和 HDTree 在 C. elegans 上的可视化差异，突出 HDTree 的 lineage inference 和真实时间结构更一致。

知乎图注：

> C. elegans case study。相比 TreeVAE，HDTree 推断出的 lineage visualization 更接近真实发育时间结构。

## 可选备图

### 图 4：Generative Validation

文件：

```text
docs/assets/zhihu/fig4_generative_validation.png
```

放置位置：“Generative validation：沿着谱系路径生成”小节后。

作用：如果文章需要更强调生成能力，可以额外加入这一张；如果担心文章太长，保留前三张即可。

知乎图注：

> HDTree 的 tree-conditioned generation。模型可以沿着 learned path 在 MNIST 和 C. elegans 上生成连续状态，用于验证 inferred lineage 的合理性。

## 发布建议

知乎正文建议使用前三张图即可。图 4 可以作为备选，如果评论区或后续文章要专门讲 generative validation，再单独展开。

