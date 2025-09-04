# 🎨 Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Contadores
PASSED=0
TOTAL=5

# Verificaciones
echo "🔍 Verificando entorno IA Core Models..."

if [ -f Dockerfile ]; then
  echo -e "${GREEN}✅ Dockerfile encontrado.${NC}"
  ((PASSED++))
else
  echo -e "${RED}❌ Dockerfile no encontrado.${NC}"
fi

if [ -f configs/requirements.txt ]; then
  echo -e "${GREEN}✅ requirements.txt encontrado en configs/${NC}"
  ((PASSED++))
else
  echo -e "${RED}❌ requirements.txt no encontrado en configs/${NC}"
fi

if [ -f training/train_cnn.py ]; then
  echo -e "${GREEN}✅ Script de entrenamiento encontrado.${NC}"
  ((PASSED++))
else
  echo -e "${RED}❌ Script de entrenamiento no encontrado.${NC}"
fi

if [ -f configs/cnn_default.yaml ]; then
  echo -e "${GREEN}✅ Configuración YAML encontrada.${NC}"
  ((PASSED++))
else
  echo -e "${RED}❌ Configuración YAML no encontrada.${NC}"
fi

if [ -f models/simple_cnn.py ]; then
  echo -e "${GREEN}✅ Modelo CNN encontrado.${NC}"
  ((PASSED++))
else
  echo -e "${RED}❌ Modelo CNN no encontrado.${NC}"
fi

# Resumen
echo -e "\n${GREEN}🔧 Checks completados: ${PASSED}/${TOTAL}${NC}"
if [ "$PASSED" -eq "$TOTAL" ]; then
  echo -e "${GREEN}🎯 Entorno validado. Listo para construir y entrenar.${NC}"
else
  echo -e "${RED}⚠️ Faltan componentes. Revisa los errores anteriores.${NC}"
  exit 1
fi
