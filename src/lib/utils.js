// Divide un array plano en una matriz de [filas x columnas]
export function createMatrix(arr, size) {
  const matrix = [];
  for (let i = 0; i < arr.length; i += size) {
    matrix.push(arr.slice(i, i + size));
  }
  return matrix;
}