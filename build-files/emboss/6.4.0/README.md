# EMBOSS 6.4.0 Docker Image

This Docker image provides **emboss 6.4.0**, a high-quality package of free, Open Source software for molecular biology.

[emboss ](http://emboss.sourceforge.net/)

---

## 📦 Included Tools

- **emboss** (6.4.0)

---

## 🐳 Usage

### Example: Smith-Waterman local alignment

```bash
# Use the Smith-Waterman algorithm to calculate the local alignment of two sequences 
water -asequence X01753.1.fa -bsequence X01755.1.fa -gapopen 10 -gapextend 0.5 -outfile alignment.water
```

