const input = `#...#...
#..#...#
..###..#
.#..##..
####...#
######..
...#..#.
##.#.#.#`;

const rows = input.split("\n");
const world = {};
world[0] = rows.flatMap((row, y) =>
  row.split("").map((col, x) => ({
    x: Number(x),
    y: Number(y),
    state: col
  }))
);

function range(world, i) {
  const arr = Object.keys(world).reduce((arr, key) => {
    return arr.concat(world[key]);
  }, []);
  const range = arr.map(cube => cube[i]);
  const min = Math.min(...range) - 1;
  const max = Math.max(...range) + 1;
  return { min, max };
}

function ranges(world) {
  const positions = Object.keys(world).map(Number);
  const zmin = Math.min(...positions) - 1;
  const zmax = Math.max(...positions) + 1;
  const { min: xmin, max: xmax } = range(world, "x");
  const { min: ymin, max: ymax } = range(world, "y");
  return {
    xmin,
    xmax,
    ymin,
    ymax,
    zmin,
    zmax
  };
}

function checkNeighbours({ world, x, y, z }) {
  world = JSON.parse(JSON.stringify(world));
  const neighbours = [];

  for (let i = z - 1; i <= z + 1; i++) {
    if (!Array.isArray(world[i])) continue;

    for (let item of world[i]) {
      if (
        item.x >= x - 1 &&
        item.x <= x + 1 &&
        item.y >= y - 1 &&
        item.y <= y + 1 &&
        item.state === "#"
      ) {
        if (item.x === x && item.y === y && z === i) {
          continue;
        }
        neighbours.push(item);
      }
    }
  }
  return neighbours.length;
}

function buildWorldSlice(slices) {
  const offsetX = -Math.min(...slices.map(cube => cube.x));
  const offsetY = -Math.min(...slices.map(cube => cube.y));
  const offsetSlices = slices.map(cube => {
    cube.x += offsetX;
    cube.y += offsetY;
    return cube;
  });
  const maxX = Math.max(...offsetSlices.map(cube => cube.x));
  const maxY = Math.max(...offsetSlices.map(cube => cube.y));
  const slice = Array(maxY + 1)
    .fill(() => Array(maxX + 1).fill("."))
    .map(fn => fn());
  for (let item of offsetSlices) {
    slice[item.y][item.x] = item.state;
  }
  return slice;
}

function printWorld(world) {
  for (let key in world) {
    if (!world?.[key]?.length) continue;
    const slice = buildWorldSlice(world[key]);
    console.log(`z=${key}`);
    console.log(slice.map(row => row.join("")).join("\n"));
  }
}

function boot(world) {
  const { xmin, xmax, ymin, ymax, zmin, zmax } = ranges(world);
  const parallelWorld = JSON.parse(JSON.stringify(world));

  for (let z = zmin; z <= zmax; z++) {
    for (let y = ymin; y <= ymax; y++) {
      for (let x = xmin; x <= xmax; x++) {
        if (!parallelWorld[z]) parallelWorld[z] = [];
        const n = checkNeighbours({
          world,
          x,
          y,
          z
        });
        if (parallelWorld[z]) {
          const idx = parallelWorld[z].findIndex(
            cube => cube.x === x && cube.y === y
          );
          const exists = idx > -1;
          const cube = exists ? parallelWorld[z][idx] : { x, y, state: "." };
          switch (cube.state) {
            case "#":
              cube.state = n === 2 || n === 3 ? "#" : ".";
              break;
            case ".":
              cube.state = n === 3 ? "#" : ".";
              break;
          }
          if (exists) {
            parallelWorld[z][idx] = { ...cube };
          } else {
            parallelWorld[z].push(cube);
          }
        } else {
          parallelWorld[z].push({ x, y, z, state: n === 3 ? "#" : "." });
        }
      }
    }
  }
  for (let key in parallelWorld) {
    if (!parallelWorld[key]) delete parallelWorld[key];
    if (parallelWorld[key].every(cube => cube.state === ".")) {
      delete parallelWorld[key];
    }
  }
  return parallelWorld;
}

function countCubes(world) {
  let count = 0;
  for (let key in world) {
    count += world[key].filter(cube => cube.state === "#").length;
  }
  return count;
}

function bootCycle(world, i = 1) {
  if (i > 6) {
    return world;
  }
  const newWorld = boot(world);
  printWorld(newWorld);
  console.log("bootcycle", i, countCubes(newWorld));
  return bootCycle(newWorld, i + 1);
}
bootCycle(world);
