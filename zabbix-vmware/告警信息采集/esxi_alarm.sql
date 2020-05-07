/*
 Navicat Premium Data Transfer

 Source Server         : 172.10.44.235
 Source Server Type    : MySQL
 Source Server Version : 50644
 Source Host           : 172.10.44.235:3306
 Source Schema         : vmware

 Target Server Type    : MySQL
 Target Server Version : 50644
 File Encoding         : 65001

 Date: 07/05/2020 14:25:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for esxi_alarm
-- ----------------------------
DROP TABLE IF EXISTS `esxi_alarm`;
CREATE TABLE `esxi_alarm`  (
  `vcenterip` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `datatorename` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '数据中心名称',
  `esxiname` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '虚拟机名称',
  `alarmname` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '告警名字',
  `alarlevel` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '告警等级',
  `alartime` datetime(0) NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '触发时间',
  PRIMARY KEY (`esxiname`, `alartime`) USING BTREE,
  UNIQUE INDEX `Unique_vm`(`esxiname`, `alartime`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'esxi alarm' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for vm_alarm
-- ----------------------------
DROP TABLE IF EXISTS `vm_alarm`;
CREATE TABLE `vm_alarm`  (
  `vcenterip` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `datatorename` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '数据中心名称',
  `vmname` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '虚拟机名称',
  `alarmname` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '告警名字',
  `alarlevel` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '告警等级',
  `alartime` datetime(0) NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '触发时间',
  PRIMARY KEY (`vmname`, `alartime`) USING BTREE,
  UNIQUE INDEX `Unique_vm`(`vmname`, `alartime`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'vm alarm' ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
