#!/usr/bin/node

if (process.argv.length <= 3)
{
    console.log(0);
}
else
{
    const res = process.argv.slice(3, process.argv.length);
    res.sort((a, b) => parseInt(a) - parseInt(b));
    res.reverse();
    console.log(res[1]);
}
