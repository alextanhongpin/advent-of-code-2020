const input = `#...#...
#..#...#
..###..#
.#..##..
####...#
######..
...#..#.
##.#.#.#`;

const rows = input.split("\n");
const world = rows.flatMap((row, y) =>
  row.split("").map((col, x) => ({
    x: Number(x),
    y: Number(y),
    z: 0,
    w: 0,
    state: col
  }))
);

function buildRange(world, attr) {
  const positions = Array.from(new Set(world.map(cube => cube[attr])));
  return {
    min: Math.min(...positions) - 1,
    max: Math.max(...positions) + 1
  };
}

function findNeighbours({ world, x, y, z }) {
  const cubes = world.filter(cube => {
    const validX = cube.x >= x - 1 && cube.x <= x + 1;
    const validY = cube.y >= y - 1 && cube.y <= y + 1;
    const validZ = cube.z >= z - 1 && cube.z <= z + 1;
    const center = cube.x === x && cube.y === y && cube.z === z;
    const isActive = cube.state === "#";
    return validX && validY && validZ && isActive && !center;
  });
  return cubes.length;
}
function findNeighbours4d({ world, x, y, z, w }) {
  const cubes = world.filter(cube => {
    const validX = cube.x >= x - 1 && cube.x <= x + 1;
    const validY = cube.y >= y - 1 && cube.y <= y + 1;
    const validZ = cube.z >= z - 1 && cube.z <= z + 1;
    const validW = cube.w >= w - 1 && cube.w <= w + 1;
    const center = cube.x === x && cube.y === y && cube.z === z && cube.w === w;
    const isActive = cube.state === "#";
    return validX && validY && validZ && validW && isActive && !center;
  });
  return cubes.length;
}

function boot(world) {
  const parallelWorld = JSON.parse(JSON.stringify(world));
  const xrange = buildRange(world, "x");
  const yrange = buildRange(world, "y");
  const zrange = buildRange(world, "z");

  for (let z = zrange.min; z <= zrange.max; z++) {
    for (let y = yrange.min; y <= yrange.max; y++) {
      for (let x = xrange.min; x <= xrange.max; x++) {
        const n = findNeighbours({ world, x, y, z });
        const idx = parallelWorld.findIndex(
          cube => cube.x === x && cube.y === y && cube.z === z
        );
        const exists = idx > -1;
        const cube = exists ? parallelWorld[idx] : { x, y, z, state: "." };
        switch (cube.state) {
          case "#":
            cube.state = n === 2 || n === 3 ? "#" : ".";
            break;
          case ".":
            cube.state = n === 3 ? "#" : ".";
            break;
        }
        if (!exists) {
          parallelWorld.push(cube);
        }
      }
    }
  }
  return parallelWorld.filter(cube => cube.state === "#");
}

function boot4d(world) {
  const parallelWorld = JSON.parse(JSON.stringify(world));
  const xrange = buildRange(world, "x");
  const yrange = buildRange(world, "y");
  const zrange = buildRange(world, "z");
  const wrange = buildRange(world, "w");

  for (let w = wrange.min; w <= wrange.max; w++) {
    for (let z = zrange.min; z <= zrange.max; z++) {
      for (let y = yrange.min; y <= yrange.max; y++) {
        for (let x = xrange.min; x <= xrange.max; x++) {
          const n = findNeighbours4d({ world, w, x, y, z });
          const idx = parallelWorld.findIndex(
            cube => cube.x === x && cube.y === y && cube.z === z && cube.w === w
          );
          const exists = idx > -1;
          const cube = exists ? parallelWorld[idx] : { w, x, y, z, state: "." };
          switch (cube.state) {
            case "#":
              cube.state = n === 2 || n === 3 ? "#" : ".";
              break;
            case ".":
              cube.state = n === 3 ? "#" : ".";
              break;
          }
          if (!exists) {
            parallelWorld.push(cube);
          }
        }
      }
    }
  }
  return parallelWorld.filter(cube => cube.state === "#");
}

function bootCycle(world, bootFn = boot, cycle = 0) {
  if (cycle < 6) {
    return bootCycle(bootFn(world), bootFn, cycle + 1);
  }
  return world;
}

const finalWorld = bootCycle(world);
console.log(finalWorld.length);

// The only difference is an additional loop for the 4th dimension.
const finalWorld2 = bootCycle(world, boot4d);
console.log(finalWorld2.length);
