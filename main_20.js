const fs = require("fs");

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

// There are actually 16 possible transformations, but they are repeating.
// Flip vertical, flip both and the rotations for each of them is excluded.
const TILES = {
  none: original => original,
  rotate90: rotate90anticlockwise,
  rotate180: arr => rotate90anticlockwise(rotate90anticlockwise(arr)),
  rotate270: arr =>
    rotate90anticlockwise(rotate90anticlockwise(rotate90anticlockwise(arr))),
  flipHorizontal,
  flipHorizontalRotate90: arr => rotate90anticlockwise(flipHorizontal(arr)),
  flipHorizontalRotate180: arr =>
    rotate90anticlockwise(rotate90anticlockwise(flipHorizontal(arr))),
  flipHorizontalRotate270: arr =>
    rotate90anticlockwise(
      rotate90anticlockwise(rotate90anticlockwise(flipHorizontal(arr)))
    )
};

function flipHorizontal(tile) {
  return [...tile].map(t => [...t].reverse());
}

function rotate90anticlockwise(arr) {
  arr = [...arr].map(row => [...row]);
  const n = Math.floor(arr.length / 2);
  for (let i = 0; i < n; i++) {
    for (let j = i; j < arr.length - i - 1; j++) {
      const tmp = arr[i][j];
      arr[i][j] = arr[j][arr.length - i - 1];
      arr[j][arr.length - i - 1] = arr[arr.length - i - 1][arr.length - j - 1];
      arr[arr.length - i - 1][arr.length - j - 1] = arr[arr.length - j - 1][i];
      arr[arr.length - j - 1][i] = tmp;
    }
  }
  return arr;
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
      return this;
    }
    this._transformations[name] = TILES[name](this.original);
    this.tile = this._transformations[name];
    return this;
  }
  positions(tile) {
    return tile;
  }
  get top() {
    return this.positions(this.tile[0]).join("");
  }
  get bottom() {
    return this.positions(this.tile[this.tile.length - 1]).join("");
  }
  get left() {
    const left = [];
    for (let tile of this.tile) {
      left.push(tile[0]);
    }
    return this.positions(left).join("");
  }
  get right() {
    const right = [];
    for (let tile of this.tile) {
      right.push(tile[tile.length - 1]);
    }
    return this.positions(right).join("");
  }
  toString() {
    return this.tile.map(row => row.join("")).join("\n");
  }
  buildOrientation() {
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
      if (i > 0 && i < max && j > 0 && j < max) {
        // All 4 edges must have connecting points.
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
      let set = new Set(tileIds);
      set.delete(tileId);
      const result = placeTile(tiles, [...set], grid, n + 1, cache);
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
  const dim = Math.sqrt(Object.keys(tiles).length);
  const output = Array(dim)
    .fill(() => Array(dim).fill(null))
    .map(fn => fn());
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
  const result = placeTile(tiles, Object.keys(tiles), output, 0, cache);
  const ids = result.map(row => row.map(tile => Number(tile.id)));

  const corners = [
    ids[0][0],
    ids[0][ids.length - 1],
    ids[ids.length - 1][0],
    ids[ids.length - 1][ids.length - 1]
  ];
  return corners.reduce((a, b) => a * b);
}

console.time();
console.log(solver(testInput));
console.timeEnd();

console.time();
console.log(solver(input));
console.timeEnd();
