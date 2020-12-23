const fs = require("fs");

class Matrix {
  static new(n) {
    return Array(n)
      .fill(() => Array(n).fill(null))
      .map(fn => fn());
  }
  static clone(m) {
    return m.map(n => [...n]);
  }
  static flipHorizontal(m) {
    return Matrix.clone(m).map(row => row.reverse());
  }
  static rotate90(m) {
    m = Matrix.clone(m);
    const n = Math.floor(m.length / 2);
    for (let i = 0; i < n; i++) {
      for (let j = i; j < m.length - i - 1; j++) {
        const tmp = m[i][j];
        m[i][j] = m[j][m.length - i - 1];
        m[j][m.length - i - 1] = m[m.length - i - 1][m.length - j - 1];
        m[m.length - i - 1][m.length - j - 1] = m[m.length - j - 1][i];
        m[m.length - j - 1][i] = tmp;
      }
    }
    return m;
  }

  // There are actually 16 possible transformations, but they are repeating.
  // Flip vertical, flip both and the rotations for each of them is excluded.
  static TRANSFORMATIONS = {
    none: m => m,
    rotate90: Matrix.rotate90,
    rotate180: m => Matrix.rotate90(Matrix.rotate90(m)),
    rotate270: m => Matrix.rotate90(Matrix.rotate90(Matrix.rotate90(m))),
    flipHorizontal: Matrix.flipHorizontal,
    flipHorizontalRotate90: m => Matrix.rotate90(Matrix.flipHorizontal(m)),
    flipHorizontalRotate180: m =>
      Matrix.rotate90(Matrix.rotate90(Matrix.flipHorizontal(m))),
    flipHorizontalRotate270: m =>
      Matrix.rotate90(
        Matrix.rotate90(Matrix.rotate90(Matrix.flipHorizontal(m)))
      )
  };
  static transform(transformation, m) {
    return Matrix.TRANSFORMATIONS[transformation](Matrix.clone(m));
  }
}

class Tile {
  constructor(id, tile) {
    this.id = id;
    this.original = [...tile];
    this.tile = [...tile];
    this.width = this.tile[0].length;
    this.height = this.tile.length;
    this._transformations = {};
  }
  transform(name) {
    if (this._transformations[name]) {
      this.tile = this._transformations[name];
    } else {
      this._transformations[name] = Matrix.transform(name, this.original);
      this.tile = this._transformations[name];
    }
    return this;
  }
  get top() {
    return this.tile[0].join("");
  }
  get bottom() {
    return this.tile[this.tile.length - 1].join("");
  }
  get left() {
    const left = [];
    for (let tile of this.tile) {
      left.push(tile[0]);
    }
    return left.join("");
  }
  get right() {
    const right = [];
    for (let tile of this.tile) {
      right.push(tile[tile.length - 1]);
    }
    return right.join("");
  }

  toString() {
    return this.tile.map(row => row.join("")).join("\n");
  }

  buildOrientation() {
    // Without performing the transformations, we can just reverse each edges
    // to get the combinations.
    const ori = [this.left, this.right, this.bottom, this.top];
    const reversed = ori.map(reverse);
    return [...ori, ...reversed];
  }

  get orientations() {
    if (this._orientations) return Object.keys(this._orientations);
    this._orientations = {};
    const orientations = this.buildOrientation();
    for (let orientation of orientations) {
      this._orientations[orientation] = true;
    }
    return Object.keys(this._orientations);
  }

  hasOrientation(o) {
    return this._orientations[o];
  }
}

function reverse(str) {
  return str
    .split("")
    .reverse()
    .join("");
}

function parseInput(input) {
  const tiles = {};
  let tile = null;
  for (let line of input) {
    line = line.trim();
    if (!line.length) continue;
    const matches = Array.from(line.matchAll(/Tile (\d+):/g), m => m[1]);
    const match = matches?.[0];
    if (match) {
      tile = match;
      continue;
    }
    if (!tiles[tile]) tiles[tile] = [];
    tiles[tile].push(line.split(""));
  }
  return tiles;
}

const TRANSFORMATIONS = [
  "none",
  "rotate90",
  "rotate180",
  "rotate270",
  "flipHorizontal",
  "flipHorizontalRotate90",
  "flipHorizontalRotate180",
  "flipHorizontalRotate270"
];

function placeTile(tiles, tileIds, grid, n = 0, cache = {}) {
  if (!tileIds.length) {
    return grid;
  }
  const i = Math.floor(n / grid.length); // Row.
  const j = n % grid.length; // Column.
  const max = grid.length - 1;

  for (let tileId of tileIds) {
    const tile = tiles[tileId];
    if (i > 0 && i < max) {
      const prevBtm = grid[i - 1][j].bottom;
      if (!tile.hasOrientation(prevBtm)) {
        continue;
      }
    }

    if (j > 0 && j < max) {
      const prevRight = grid[i][j - 1].right;
      if (!tile.hasOrientation(prevRight)) {
        continue;
      }
    }

    for (let transformation of TRANSFORMATIONS) {
      const curr = tile.transform(transformation);

      const hasTop = cache[curr.top].length > 0;
      const hasBottom = cache[curr.bottom].length > 0;
      const hasLeft = cache[curr.left].length > 0;
      const hasRight = cache[curr.right].length > 0;

      // Any tiles placed in the center must have 4 edges.
      if (i > 0 && i < max && j > 0 && j < max) {
        const hasAll = hasTop && hasBottom && hasLeft && hasRight;
        if (!hasAll) {
          continue;
        }
      }
      // Top left. Right and bottom must connect.
      if (i === 0 && j === 0) {
        if (!(hasRight && hasBottom)) {
          continue;
        }
      }
      // Top right. Left and bottom must connect.
      if (i === 0 && j === max) {
        if (!(hasLeft && hasBottom)) {
          continue;
        }
      }
      // Bottom left. Top and right must connect.
      if (i === max && j === 0) {
        if (!(hasTop && hasRight)) {
          continue;
        }
      }
      // Bottom right. Top and left must connect.
      if (i === max && j === 0) {
        if (!(hasTop && hasLeft)) {
          continue;
        }
      }
      if (i > 0) {
        const prevBtm = grid[i - 1][j].bottom;
        const currTop = curr.top;
        if (prevBtm !== currTop) continue;
      }
      if (j > 0) {
        const prevRight = grid[i][j - 1].right;
        const currLeft = curr.left;
        if (prevRight !== currLeft) continue;
      }
      grid[i][j] = curr;
      const result = placeTile(
        tiles,
        tileIds.filter(id => id !== tileId),
        grid,
        n + 1,
        cache
      );
      if (result.flatMap(arr => arr).every(Boolean)) {
        return grid;
      } else {
        grid[i][j] = null;
      }
    }
  }
  return grid;
}

function solver(input) {
  const tiles = parseInput(input);
  for (let id in tiles) {
    tiles[id] = new Tile(id, tiles[id]);
  }

  const cache = {};
  const populate = (key, value) => {
    if (!cache[key]) cache[key] = [];
    cache[key].push(value);
    cache[key] = [...new Set(cache[key])];
  };

  for (let tileId of Object.keys(tiles)) {
    const orientations = tiles[tileId].orientations;
    for (let o of orientations) {
      populate(o, tileId);
    }
  }

  const n = Math.sqrt(Object.keys(tiles).length);
  const result = placeTile(tiles, Object.keys(tiles), Matrix.new(n), 0, cache);
  const ids = result.map(row => row.map(tile => Number(tile.id)));

  const corners = [
    ids[0][0],
    ids[0][ids.length - 1],
    ids[ids.length - 1][0],
    ids[ids.length - 1][ids.length - 1]
  ];
  console.log("Part 1:", corners.reduce((a, b) => a * b));

  const dragon = `                  # 
#    ##    ##    ###
 #  #  #  #  #  #   `;
  const dragonMatrix = dragon.split("\n").map(row => row.split(""));
  const dragonPositions = dragonMatrix.flatMap((body, y) => {
    return body.flatMap((tile, x) => (tile === "#" ? { x, y } : []));
  });
  const dragonHeight = dragonMatrix.length;
  const dragonWidth = dragonMatrix[0].length;

  const image = result
    .map(row => {
      row = [...row];
      const image = Array(row[0].tile.length - 2)
        .fill(() => [])
        .map(fn => fn());
      for (let tile of row) {
        for (let i = 1; i < tile.tile.length - 1; i++) {
          image[i - 1].push(...tile.tile[i].slice(1, tile.tile[i].length - 1));
        }
      }
      const result = image.map(row => row.join("")).join("\n");
      return result;
    })
    .join("\n");
  const imageMatrix = image.split("\n").map(row => row.split(""));

  for (let transformation of TRANSFORMATIONS) {
    const rotated = Matrix.transform(transformation, imageMatrix);

    let matches = 0;
    for (let y = 0; y < rotated.length - dragonHeight; y++) {
      for (let x = 0; x < rotated[y].length - dragonWidth; x++) {
        const match = dragonPositions.every(
          position => rotated[y + position.y][x + position.x] === "#"
        );
        if (match) {
          dragonPositions.every(
            position => (rotated[y + position.y][x + position.x] = "O")
          );
          matches++;
        }
      }
    }
    if (matches) {
      let total = 0;
      for (let i = 0; i < rotated.length; i++) {
        for (let j = 0; j < rotated[i].length; j++) {
          total += rotated[i][j] === "#";
        }
      }
      console.log(
        `Part 2: found ${matches} dragons with water roughness ${total}`
      );
    }
  }
}

function main() {
  const input = fs.readFileSync("input_20.txt", "utf8").split("\n");

  const testInput = `Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...`.split("\n");

  console.time();
  solver(testInput);
  console.timeEnd();

  console.time();
  solver(input);
  console.timeEnd();
}
main();
